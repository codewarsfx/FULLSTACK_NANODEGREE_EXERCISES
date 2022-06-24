from ast import dump
from marshmallow import Schema, fields

from utils import hash_password 

class Userschema(Schema):
    class Meta:
         ordered = True
    id = fields.Integer(dump_only=True)
    name = fields.String(required= True)
    email = fields.Email(required= True)
    created_at = fields.DateTime(required= True,dump_only=True)
    password = fields.Method(required= True,deserialize="hash_password")

    def hash_password(self, password):
        return hash_password(password)               


