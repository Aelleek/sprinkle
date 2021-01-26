"""
  __init__.py
  Sprinkle

  Created by LeeKW on 2021/01/26.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    # kochat.app.template_folder = kochat.root_dir + 'templates'
    # kochat.app.static_folder = kochat.root_dir + 'static'
    app.run(port=8080, host='0.0.0.0')