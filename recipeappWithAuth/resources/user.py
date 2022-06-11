from http import HTTPStatus
from flask_restful import Resource
from flask import request
from models.userModel import User
from models.recipes import Recipe

from models.userModel import User
from utils import hash_password


class UserList(Resource):
    def post(self):
        data = request.get_json()
        # check that user doesn't already exist'
        name = data.get('name')
        email = data.get('email')
        password = data.get('password') 

        if User.find_by_name(name):
            return {"message":'user with that name already exists'}, HTTPStatus.BAD_REQUEST
        
        elif User.find_by_email(email):
            return {"message":'user with that email already exists'},HTTPStatus.BAD_REQUEST
        
        hash = hash_password(password)

        newUser = User(name=data.get('name'), email=data.get('email'), password=hash)
        newUser.add()

        return newUser.format(), HTTPStatus.CREATED

        

