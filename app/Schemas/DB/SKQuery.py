import psycopg2
from System.Config import connect_database
from datetime import datetime
import inspect

class NewSKQuery:
    def __init__(self):
        self.commands = []
        self.params = []
        self.named_params = []

    def Add(self, command):
        self.commands.append(command)
        self.params.append(None)
        self.named_params.append({})

    def Open(self, fetch="all"):
        procedure_name = self.get_caller_name()
        try:
            connection = connect_database()
            cur = connection.cursor()

            result = {}

            for command, params, named_params in zip(self.commands, 
                                                     self.params, 
                                                     self.named_params):
                if named_params:
                    command, params = self._convert_named_params(command, named_params)
                cur.execute(command, params)

                if fetch == "one":
                    row = cur.fetchone()
                    if row:
                        result = {cur.description[i][0]: row[i] for i in range(len(row))}
                elif fetch == "all":
                    raise ValueError("fetch='all' não é suportado para retornar um único dicionário")

            connection.commit()
            cur.close()

            self.LogSQL(procedure_name)
            
            return result
        
        except psycopg2.Error as error:
            self.LogSQL(procedure_name, str(error))
        finally:
            connection.close()

    def Execute(self):
        procedure_name = self.get_caller_name()
        try:
            connection = connect_database()
            cur = connection.cursor()

            for command, params, named_params in zip(self.commands, self.params, self.named_params):
                if named_params:
                    command, params = self._convert_named_params(command, named_params)
                cur.execute(command, params)

            connection.commit()
            cur.close()
            self.LogSQL(procedure_name)
            
        except psycopg2.Error as error:
            self.LogSQL(procedure_name, str(error))
            print("Erro ao executar o comando:", error)

        finally:
            connection.close()

    def set_params(self, params):
        if self.commands:
            self.params[-1] = params
        else:
            raise IndexError("Nenhuma query foi adicionada para definir os parâmetros.")

    def ParamByName(self, name, value):
        if self.named_params:
            self.named_params[-1][name] = value
        else:
            raise IndexError("Nenhuma query foi adicionada para definir os parâmetros nomeados.")

    def _convert_named_params(self, query, named_params):
        converted_query = query
        params = []
        missing_params = []
        for name in self._extract_param_names(query):
            if name not in named_params:
                missing_params.append(name)
            else:
                placeholder = f":{name}"
                if placeholder in converted_query:
                    converted_query = converted_query.replace(placeholder, "%s")
                    params.append(named_params[name])
        
        if missing_params:
            raise ValueError(f"Parâmetros não atribuídos: {', '.join(missing_params)}")
        
        return converted_query, params

    def _extract_param_names(self, query):
        import re
        return re.findall(r":(\w+)", query)

    def Close(self):
        self.commands = []
        self.params = []
        self.named_params = []

    def LogSQL(self, transaction, details="200"):
        print('''SQL: [ DATETIME: {} | Transaction: {} | Status: {} ]'''.
                    format(datetime.now(), transaction, details))

    def get_caller_name(self):
        frame = inspect.currentframe()
        caller_frame = frame.f_back.f_back 
        caller_name = caller_frame.f_code.co_name
        return caller_name