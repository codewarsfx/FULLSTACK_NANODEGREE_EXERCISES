from ast import dump
from typing_extensions import Required
from marshmallow import Schema, fields

from utils import hash_password 

class Userschema(Schema):
    id = fields.Integer(required= True)
    name = fields.String(required= True)
    email = fields.Email(required= True,dump_only=True)
    created_at = fields.DateTime(required= True,dump_only=True)
    password = fields.Password(required= True,deserialize="compare_password")

    def compare_password(self, password):
        return hash_password(password)


