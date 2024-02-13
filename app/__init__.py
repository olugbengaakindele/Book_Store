# app/init
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(env):

    myapp = Flask(__name__)
    config_file = os.path.join(os.getcwd(),'config',f'{env}.py')
    myapp.config.from_pyfile(config_file)

    db.init_app(myapp)

    from app.auth import auth
    myapp.register_blueprint(auth)

    from app.catlog import cat
    myapp.register_blueprint(cat)





    return myapp



