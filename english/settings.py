import os
from dotenv import load_dotenv
from pathlib import Path

#  os
# load_dotenv(dotenv_path=os.path.join(os.getcwd(), '.env'))
#  Path
load_dotenv(dotenv_path=Path('.') / '.env')


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    SECRET_KEY = os.urandom(32)
    TEMPLATES_AUTO_RELOAD = os.getenv('TEMPLATES_AUTO_RELOAD')
    DEBUG = False
    TESTING = os.getenv('TESTING')


class ConfigDebug(Config):
    FLASK_APP = os.getenv('FLASK_APP')
    DEBUG = os.getenv('DEBUG')
    SERVER_NAME = os.getenv('SERVER_NAME')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')


class ConfigProd(Config):
    PROPAGATE_EXCEPTIONS = os.getenv('PROPAGATE_EXCEPTIONS')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
