"""
  __init__.py
  Sprinkle

  Created by LeeKW on 2021/01/26.
"""
# -*- coding: utf-8 -*- 

from flask import Flask
from pymongo import MongoClient

import sys
import config


app = Flask(__name__)

# app.config.from_envvar('APP_CONFIG_FILE')

# ‘환경 변수 APP_CONFIG_FILE에 정의된 파일을 환경 파일로 사용하겠다’는 의미이다.


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/users')
def getUsers():
    client = MongoClient(app.config.MONGO_DATABASE_URI)
    data = client.sprinkle.member.find()
    for i in data:
          print(i)
    return "성공"



if __name__ == '__main__':
    # kochat.app.template_folder = kochat.root_dir + 'templates'
    # kochat.app.static_folder = kochat.root_dir + 'static'
    # app.config["MONGO_URI"] = "mongodb://sprinkle:bitbitr35@localhost:27017/sprinkle"
    
    # mongo = PyMongo(app)

    env = sys.argv[1] if len(sys.argv) > 2 else 'dev'
    
    if env == 'dev':
        app.config = config.DevelopmentConfig
    elif env == 'test':
        app.config = config.TestConfig
    elif env == 'prod':
        app.config = config.ProductionConfig
    else:
        raise ValueError('Invalid environment name')
   

    app.run(port=8080, host='0.0.0.0')


    # https://mingrammer.com/ways-to-manage-the-configuration-in-python/