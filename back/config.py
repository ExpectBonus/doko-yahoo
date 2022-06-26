import os

class DevelopmentConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    """SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/flask_sample?charset=utf8'.format(**{
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'host': os.getenv('DB_HOST', 'localhost'),
    })"""
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@db:5432/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

class TestConfig:

    # Flask
    TESTING = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False