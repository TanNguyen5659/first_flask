from marshmallow import Schema, fields

class CarSchema(Schema):
    id = fields.Str(dump_only=True)
    make = fields.Str(required = True)
    model = fields.Str(required = True)
    password = fields.Str(required = True, load_only=True)


class PostSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str()
    body = fields.Str(required=True)
    vehicle = fields.Int(required=True)