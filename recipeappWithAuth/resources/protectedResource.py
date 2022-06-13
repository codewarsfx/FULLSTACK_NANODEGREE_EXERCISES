
from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.userModel import User
from flask_jwt_extended import jwt_required, get_jwt_identity


class Protected(Resource):
    @jwt_required(optional=True)
    def get(self,name):

        user_id = get_jwt_identity()
        print(user_id)
        userWithToken = User.query.filter(User.id == user_id).first()
       
        if  userWithToken and userWithToken.name == name:
            return userWithToken.format(),HTTPStatus.OK
        else:
            return {
                "message":"you are not allowed to view this resource"
            }, HTTPStatus.UNAUTHORIZED

   