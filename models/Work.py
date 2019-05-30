from app import db
from pony.orm import Required, Optional, Set
from marshmallow import Schema, fields, post_load
from datetime import datetime, timedelta



class Work(db.Entity):
    createdBy = Required('User')
    created = Required(str)
    name = Required(str)
    iframe = Optional(str)
    embed = Optional(str)
    picture = Optional(str)
    github = Optional(str)
    code = Optional(str)
    description = Required(str)
    medium = Set('Medium')


class WorkSchema(Schema):
    id = fields.Int(dump_only=True)
    createdBy = fields.Nested('UserSchema', exclude=('works', 'email'), dump_only=True)
    created = fields.Str(required=True)
    name = fields.Str(required=True)
    iframe = fields.Str()
    embed = fields.Str()
    picture = fields.Str()
    github = fields.Str()
    code = fields.Str()
    description = fields.Str(required=True)
    medium = fields.Nested('MediumSchema', many=True, dump_only=True)



    
