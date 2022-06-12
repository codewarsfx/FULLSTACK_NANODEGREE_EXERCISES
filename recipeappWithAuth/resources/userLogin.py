from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token
from models.userModel import User
from utils import compare_password
from http import HTTPStatus


class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        # find user with the email
        user = User.find_by_email(email)

        if not user or compare_password(user.password,password):
            return {"message":"invalid login credentials"}, 401

        else:
            jwt_token = create_access_token(identity= user.id)
            return {"message":"success", "token":jwt_token}, HTTPStatus.OK
      

        