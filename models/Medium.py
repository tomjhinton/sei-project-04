from app import db
from pony.orm import Required, Set, Optional
from marshmallow import Schema, fields

# The model describes the database table
class Medium(db.Entity):
    name = Required(str)
    works = Set('Work')
    ads = Set('Ad') # Describes the Many side of a 1:M reationship
    createdBy = Optional('User')

# The `schema` descibes the serialization/deserialization
class MediumSchema(Schema):
    id = fields.Int(dump_only=True) # dump_only means "write only"
    name = fields.Str(required=True)
    work = fields.Nested('WorkSchema', many=True, exclude=('user',))
    ad = fields.Nested('Adschema', many=True, exclude=('user',))
    createdBy = fields.Nested('UserSchema', exclude=('works', 'email'), dump_only=True)
