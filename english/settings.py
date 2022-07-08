import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path('.') / '.env')

driver = os.getenv('DRIVER_DB')
name_db = os.getenv('NAME_DB')
port = os.getenv('PORT_DB')
username = os.getenv('USER_DB')
password = os.getenv('PASSWORD_DB')
server_name = os.getenv('SERVER_NAME')


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.urandom(32)
    TEMPLATES_AUTO_RELOAD = True
    DEBUG = False
    TESTING = False


class ConfigDebug(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///english_app.db'


class ConfigProd(Config):
    PROPAGATE_EXCEPTIONS = os.getenv('PROPAGATE_EXCEPTIONS')
    SQLALCHEMY_DATABASE_URI = f'{driver}://{username}:{password}@{server_name}:{port}/{name_db}'
