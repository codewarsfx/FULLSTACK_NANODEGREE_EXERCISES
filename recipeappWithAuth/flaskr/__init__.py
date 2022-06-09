from flask import Flask
from config import Config
from flask_migrate import Migrate
from extensions import db
from flask_restful import Api
from resources.user import UserList

def create_app():
    app = Flask(__name__)
    register_db(app)
    register_api(app)


def register_db(app):
   app.config.from_object(Config)
   db.init_app(app)
   migrate = Migrate(app,db)

def register_api(app):
    api = Api(app)
    api.add_resource(UserList,'/api/users')


