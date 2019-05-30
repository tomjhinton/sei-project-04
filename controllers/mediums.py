from flask import Blueprint, request, jsonify, abort
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Medium import Medium, MediumSchema
from lib.secure_route import secure_route


router = Blueprint(__name__, 'mediums') # creates a router for this controller

@router.route('/mediums', methods=['GET'])
@db_session # Allows access to the database in the `index` function
def index():
    # This will serialize our data
    # `many=True` because there are many mediums, ie we expect a list
    schema = MediumSchema(many=True)
    mediums = Medium.select() # get all the mediums
    return schema.dumps(mediums) # `schema.dumps` converts the list to JSON


@router.route('/mediums', methods=['POST'])
@db_session
@secure_route
def create():
    # This will deserialize the JSON from insomnia
    schema = MediumSchema()

    try:
        # attempt to convert the JSON into a dict
        data = schema.load(request.get_json())
        # Use that to create a medium object
        medium = Medium(**data)
        # store it in the database
        db.commit()
    except ValidationError as err:
        # if the validation fails, send back a 422 response
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    # otherwise, send back the medium data as JSON
    return schema.dumps(medium), 201


@router.route('/mediums/<int:bread_id>', methods=['GET'])
@db_session
def show(medium_id):
    # This will serialize our data
    schema = MediumSchema()
    # This gets a medium by ID
    medium = Medium.get(id=medium_id)

    # If we can't find a medium, send a 404 response
    if not medium:
        abort(404)

    # otherwise, send back the medium data as JSON
    return schema.dumps(medium)


@router.route('/mediums/<int:medium_id>', methods=['PUT'])
@db_session
@secure_route
def update(medium_id):
    schema = MediumSchema()
    medium = Medium.get(id=medium_id)

    if not medium:
        abort(404)

    try:
        data = schema.load(request.get_json())
        medium.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(medium)


@router.route('/mediums/<int:medium_id>', methods=['DELETE'])
@db_session
@secure_route
def delete(medium_id):
    medium = Medium.get(id=medium_id)

    if not medium:
        abort(404)

    medium.delete()
    db.commit()

    return '', 204
