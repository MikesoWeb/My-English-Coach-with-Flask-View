import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite://memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.urandom(32)
    MSEARCH_ENABLE = True
    MSEARCH_INDEX_NAME = 'msearch'
    MSEARCH_PRIMARY_KEY = 'id'
    TEMPLATES_AUTO_RELOAD = False
    DEBUG = False
    TESTING = False


class ConfigDebug(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    # SERVER_NAME = 'localhost:5567'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///english_app.db'


class ConfigProd(Config):
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///english_db1.db'
