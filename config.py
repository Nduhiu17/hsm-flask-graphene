import datetime
import os


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    JWT_SECRET_KEY = "dfgdfgdfg"
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    DEBUG = True


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    SECRET_KEY = os.environ['SECRET_KEY']
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    SECRET_KEY = "this-is-secret"
    TESTING = True


app_config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
