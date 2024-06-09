''' Função que recebe um dict e 
    verifica se todos os campos estão preenchidos '''
def fields_empty(dict:dict) -> list:
    try:
        for field in dict:
            if not dict[field]: return True
        return False

    except Exception as error:
        print(str(error))