from dataclasses import field
from marshmallow import Schema, fields, post_dump, validate, validates,ValidationError
from userschema import UserSchema


def validate_num_of_servings(n):
 if n < 1:
    raise ValidationError('Number of servings must be greater than0.')
 if n > 50:
    raise ValidationError('Number of servings must not be greater than 50.')
class RecipeSchema(Schema):
    class Meta:
     ordered = True
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=[validate.
    Length(max=100)])
    time=fields.DateTime(required=True, validate=[validate])
    description = fields.String(validate=[validate.Length(max=200)])
    num_of_servings = fields.Integer(validate=validate_num_of_servings)
    cook_time = fields.Integer()
    directions = fields.String(validate=[validate.Length(max=1000)])
    is_publish = fields.Boolean(dump_only=True)
    author = fields.Nested(UserSchema, attribute='user', dump_only=True,
    only=['id', 'username'])
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)