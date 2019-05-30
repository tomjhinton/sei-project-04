from app import db
from pony.orm import Required, Set, Optional
from marshmallow import Schema, fields
from datetime import datetime, timedelta







class Ad(db.Entity):
    createdBy = Required('User')
    created = Required(str)
    description = Required(str)
    medium = Set('Medium')
    languages = Optional(str)
    timeframe = Optional(float)
    budget = Optional(float)
    name = Required(str)



class AdSchema(Schema):
    id = fields.Int(dump_only=True) # dump_only means "write only"
    name = fields.Str(required=True)
    created = fields.Str()
    createdBy = fields.Nested('UserSchema', exclude=('works', 'email'), dump_only=True)
    description = fields.Str(required=True)
    languages = fields.Str()
    name = fields.Str()
    medium = fields.Nested('MediumSchema', many=True, dump_only=True)
    timeframe = fields.Float()
