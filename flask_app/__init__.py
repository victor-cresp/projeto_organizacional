import os
from flask import Flask

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY = 'dev'
        #Database
    )

    if test_config:
        app.config.from_mapping(test_config)
    app.config.from_pyfile('config.py', silent = True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app