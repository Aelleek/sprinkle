"""
  config.py
  Sprinkle

  Created by LeeKW on 2021/01/27.
"""


class Config:
    APP_NAME = "Sprinkle"
    SECRET_KEY = 'DEFAULT'
    ADMIN_NAME = "sprinkle-admin"

    STATIC_PREFIX_PATH = "static"
    
    MONGODB_NAME = "sprinkle"
    MONGODB_ID = "sprinkle"
    MONGODB_PWD = "bitbitr35"
    MONGODB_HOST = "localhost"
    MONGODB_PORT = "27017"

    MONGO_DATABASE_URI = 'mongodb://{DB_ID}:{DB_PWD}@{MONGODB_HOST}:{MONGODB_PORT}/{DB_NAME}'

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(Config):
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False