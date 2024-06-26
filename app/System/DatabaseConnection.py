import psycopg2
from urllib.parse import urlparse
from System.Secrets import DATABASE_URI

def connect_database():
    DATABASE_URI_DICT = extract_database_info(DATABASE_URI)
    try:
        connection = psycopg2.connect(
            host = DATABASE_URI_DICT["HOST"],
            database = DATABASE_URI_DICT["DATABASE"],
            user = DATABASE_URI_DICT["USER"],
            password = DATABASE_URI_DICT["PASSWORD"]
    )
        return connection
    except Exception as error:
        print(error)

def extract_database_info(DATABASE_URI: str):
    parsed_uri = urlparse(DATABASE_URI)
    return { "HOST": str(parsed_uri.hostname), 
             "PORT":str(parsed_uri.port),
             "DATABASE":str(parsed_uri.path[1:]),
             "USER":str(parsed_uri.username),
             "PASSWORD":str(parsed_uri.password)
    }