''' Importação das configurações e serviços '''
from System.Config import *
from Schemas.DB.SKQuery import NewSKQuery

class NewSKDatabase():
    def initialize_database_connection():
        Q:NewSKQuery = NewSKQuery();
        try:
            Q.Add( '''CREATE TABLE IF NOT EXISTS "User"(
                      id SERIAL PRIMARY KEY,
                      fullname TEXT NOT NULL,
                      username TEXT UNIQUE NOT NULL,
                      email TEXT UNIQUE NOT NULL,
                      password TEXT NOT NULL,
                      register_date TIMESTAMP DEFAULT (current_timestamp)
                    );
                ''')
            Q.Execute();
        finally:
            Q.Close();
            
    def drop_tables():
        Q:NewSKQuery = NewSKQuery();
        try:
            for table in NewSKDatabase.get_tablenames():
                Q.Add('''DROP TABLE 
                         IF EXISTS "public"."{}" 
                         CASCADE'''.format(table))
                Q.Execute();
        finally:
            Q.Close();

    def get_tablenames():
        Q:NewSKQuery = NewSKQuery();
        try:
            Q.Add('''SELECT table_name 
                     FROM information_schema.tables 
                     WHERE table_type = 'BASE TABLE' 
                     AND table_schema = 'public' ''');
        
            records = Q.Open();
            return [ record[0] for record in records  ]
        finally:
            Q.Close();