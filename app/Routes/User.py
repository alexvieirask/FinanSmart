
from System.Config import *
from Schemas.Global.SKException import SKException
from System.Forms import *
from Schemas.DB.SKQuery import *

class AuthUser:
    @staticmethod
    def ValidateCredentials(email:str,password:str) -> bool:
        Q:NewSKQuery = NewSKQuery();
        try:
            Q.Add('''SELECT password 
                     FROM "public"."User" 
                     WHERE email = :EMAIL ''' );
            
            Q.ParamByName("EMAIL",email);

            user = Q.Open(fetch="one");

            if user:
                password = check_password_hash(user["password"],password)
                if password:
                    return True
                return False
        finally:
            Q.Close();
    
    @staticmethod
    def EmailIsValid(email:str)-> bool:
        pattern = '[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(pattern,email):
            return True
        return False
    
    @app.route("/signin/auth", methods=['POST'])
    def signin_authenticate_route():
        try:
            fields = request.get_json()

            if fields_empty(fields):
                raise SKException(777, 'Faltou preencher campos obrigatórios.')

            Q = NewSKQuery()
            try:
                Q.Add('''SELECT * 
                        FROM "public"."User" 
                        WHERE email = :EMAIL ''')

                Q.ParamByName("EMAIL", fields["useremail"])

                user = Q.Open(fetch="one")

                if not user:
                    raise SKException(777, 'Usuário não encontrado.')

                if not AuthUser.ValidateCredentials(fields["useremail"], fields["userpassword"]):
                    raise SKException(777, 'Credênciais de login incorretas.')

                access_token = create_access_token(identity=fields["useremail"])

                response = jsonify({"status": 200, "details": access_token})

            finally:
                Q.Close()

        except SKException as auth_error:
            response = auth_error.to_response()
        finally:
            return response
        
    @app.route("/signup/auth", methods = ["POST"])
    def singup_authenticate_route():
        response = ''
        try:
            fields = request.get_json()

            if fields_empty(fields):
                raise 'Faltou preencher campos obrigatórios.';
        
            Q:NewSKQuery = NewSKQuery();
            try:
                Q.Add('''SELECT * 
                        FROM "public"."User" 
                        WHERE username = :USERNAME 
                        OR email = :EMAIL''')
                Q.ParamByName("USERNAME",fields["username"])
                Q.ParamByName("EMAIL",fields["useremail"])

                user = Q.Open(fetch="one")

                if user:
                    raise SKException(777, 'E-mail ou usuário já cadastrado.')
                
                if not AuthUser.EmailIsValid(fields["useremail"]):
                    raise SKException(777, 'E-mail inválido.')
            
                if not (fields["userpassword"] == fields["userrepeatpassword"]):
                    raise SKException(777, 'Senhas não conferem.')
            
                hash_password = generate_password_hash(fields["userpassword"]).decode("UTF-8")

                Q.Close();

                Q.Add('''INSERT INTO "User" (fullname, 
                                                username, 
                                                email, 
                                                password)
                            VALUES (:FULLNAME, :USERNAME, :EMAIL, :PASSWORD)''')
                Q.ParamByName("FULLNAME",fields["fullname"])
                Q.ParamByName("USERNAME",fields["username"])
                Q.ParamByName("EMAIL",fields["useremail"])
                Q.ParamByName("PASSWORD",hash_password)

                Q.Execute();
        
                response = jsonify({"status":200, "details":"Usuário registrado no sistema."})
            finally:
                Q.Close();
        except SKException as auth_error:
                response = auth_error.to_response()
        finally:
            return response