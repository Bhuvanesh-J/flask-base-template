from marshmallow import Schema, fields


class SignupValidation(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    password = fields.String(required=True)
    gender = fields.String(required=True)
    email = fields.Email(required=True)
    dob = fields.Date(required=True)


class LoginValidation(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)







