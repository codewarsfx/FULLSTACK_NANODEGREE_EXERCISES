from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from http import HTTPStatus

from models.userModel import User


class Me(Resource):
    @jwt_required(optional=True)
    def get(self):
        userId = get_jwt_identity()
        user = User.find_by_id(userId)

        if not user:
            return {"message": "user not found"}, 404

        return user.format(), HTTPStatus.OK
        