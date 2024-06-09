''' Importações extras '''
from datetime import datetime, timedelta
import string, platform, random, os
from System.Secrets import *

''' Importações banco de dados '''
import psycopg2
from System.DatabaseConnection import *
from Schemas.DB.SKDatabase import NewSKDatabase

''' Importações Flask  '''
from flask import Flask, render_template,jsonify, request, redirect, url_for, abort,send_file, make_response,send_from_directory
from flask_cors import CORS
from flask_bcrypt import Bcrypt,generate_password_hash,check_password_hash
from flask_caching import Cache, CachedResponse

''' Configurações Flask'''
app = Flask(__name__, template_folder='../Src', static_folder='../Src/Static')

''' Configurações de Cache '''
app.config['CACHE_TYPE'] = 'simple'  
app.config['CACHE_DEFAULT_TIMEOUT'] = 3600 
cache = Cache(app)
user_caches = {}

''' Importações JWT '''
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

''' Configurações JWT '''
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=3)
jwt = JWTManager(app)
cors = CORS(app)
bcrypt = Bcrypt(app) 

''' Inicialização SKDatabase '''
with app.app_context():
    NewSKDatabase.initialize_database_connection()