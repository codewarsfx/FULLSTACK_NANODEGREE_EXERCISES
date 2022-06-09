from flask_restful import Resource

from models.userModel import User


class UserList(Resource):
    def get(self):
        return "hello"

