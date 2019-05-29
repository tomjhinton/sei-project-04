from app import db
from pony.orm import Required, Set
from marshmallow import Schema, fields

# The model describes the database table
class TypeOfWork(db.Entity):
    name = Required(str)
    sandwiches = Set('Sandwich') # Describes the Many side of a 1:M reationship

# The `schema` descibes the serialization/deserialization
class TypeOfWorkSchema(Schema):
    id = fields.Int(dump_only=True) # dump_only means "write only"
    name = fields.Str(required=True)
    work = fields.Nested('WorkSchema', many=True, exclude=('user',))
