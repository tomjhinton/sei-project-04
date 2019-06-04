from app import db
from pony.orm import Required, Set, Optional
from marshmallow import Schema, fields , post_load
from datetime import datetime, timedelta




from .Medium import Medium



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
    medium = fields.Nested('MediumSchema', many=True)
    medium_ids = fields.List(fields.Int(), load_only=True)



    @post_load
    def load_medium(self, data):

        data['medium'] = [Medium.get(id=medium_id) for medium_id in data['medium_ids']]
        del data['medium_ids']

        return data
