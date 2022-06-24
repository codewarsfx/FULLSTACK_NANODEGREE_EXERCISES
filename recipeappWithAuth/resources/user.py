from http import HTTPStatus
from flask_restful import Resource
from flask import request
from models.userModel import User
from models.recipes import Recipe

from models.userModel import User
from utils import hash_password

from schema.userschema import Userschema


user_schema = Userschema()
user_schema_noemail = Userschema(exclude=('email',))


class UserList(Resource):
    def post(self):
        json_data = request.get_json()
        # check that user doesn't already exist'
        data,errors = user_schema.load(data=json_data)

        print(data)

        # if errors:
        #     return {"message":"validation error","Error":errors},HTTPStatus.BAD_REQUEST

        if User.find_by_name(data.get('name')):
            return {"message":'user with that name already exists'}, HTTPStatus.BAD_REQUEST
        
        elif User.find_by_email(data.get('email')):
            return {"message":'user with that email already exists'},HTTPStatus.BAD_REQUEST
        

        newUser = User(**data)
        newUser.add()

        return user_schema.dump(newUser), HTTPStatus.CREATED

        

