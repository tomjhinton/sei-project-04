from app import db
from pony.orm import Required, Set, Optional
from marshmallow import Schema, fields
from datetime import datetime, timedelta







class Ad(db.Entity):
    createdBy = Required('User')
    created = Required(datetime.date)
    description = Required(str)
    typeOfWork = Required(str)
    languages = Optional(str)
    timeframe = Required(datetime)
    budget = Optional(float)



class AdSchema(Schema):
    id = fields.Int(dump_only=True) # dump_only means "write only"
    name = fields.Str(required=True)
    sandwiches = fields.Nested('SandwichSchema', many=True, exclude=('bread', 'categories', 'user'))



    createdBy = Required(user)
    created = Required(date)
    description = fields.Str
    typeOfWork = Required(str)
    languages = Optional(str)
    timeframe = Required(date)
    budget = Optional(float)
