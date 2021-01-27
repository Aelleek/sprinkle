"""
  __init__.py
  Sprinkle

  Created by LeeKW on 2021/01/26.
"""

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/users')
def getUsers():
    client = MongoClient('mongodb://sprinkle:bitbitr35@localhost:27017/sprinkle')
    data = client.sprinkle.member.find()
    for i in data:
          print(i)
    return "성공"


if __name__ == '__main__':
    # kochat.app.template_folder = kochat.root_dir + 'templates'
    # kochat.app.static_folder = kochat.root_dir + 'static'
    # app.config["MONGO_URI"] = "mongodb://sprinkle:bitbitr35@localhost:27017/sprinkle"
    
    # mongo = PyMongo(app)
    app.run(port=8080, host='0.0.0.0')