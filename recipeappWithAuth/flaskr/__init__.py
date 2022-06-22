from flask import Flask
from config import Config
from flask_migrate import Migrate
from extensions import db,jwt
from flask_restful import Api
from resources.me import Me
from resources.protectedResource import Protected
from resources.userLogin import UserLogin
from resources.user import UserList

def create_app():
    app = Flask(__name__)
    register_db(app)
    register_api(app)
    return app


def register_db(app):
   app.config.from_object(Config)
   db.init_app(app)
   migrate = Migrate(app,db)
   jwt.init_app(app)

def register_api(app):
    api = Api(app)
    api.add_resource(UserList,'/api/users')
    api.add_resource(Me, '/api/users/me')
    api.add_resource(UserLogin,'/api/users/login')
    api.add_resource(Protected, '/api/users/token/<string:name>')
 


if __name__ == '__main__':
    app= create_app()
    app.run()


