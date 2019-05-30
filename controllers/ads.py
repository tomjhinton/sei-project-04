from flask import Blueprint, request, jsonify, abort, g
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Ad import Ad, AdSchema
from lib.secure_route import secure_route


router = Blueprint(__name__, 'ads') # creates a router for this controller

@router.route('/ads', methods=['GET'])
@db_session # Allows access to the database in the `index` function
def index():
    # This will serialize our data
    # `many=True` because there are many ads, ie we expect a list
    schema = AdSchema(many=True)
    ads = Ad.select() # get all the ads
    return schema.dumps(ads) # `schema.dumps` converts the list to JSON


@router.route('/ads', methods=['POST'])
@db_session
@secure_route
def create():
    # This will deserialize the JSON from insomnia
    schema = AdSchema()

    try:
        # attempt to convert the JSON into a dict
        data = schema.load(request.get_json())
        # Use that to create a work object
        work = Ad(**data, createdBy=g.current_user)
        # store it in the database
        db.commit()
    except ValidationError as err:
        # if the validation fails, send back a 422 response
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    # otherwise, send back the work data as JSON
    return schema.dumps(work), 201


@router.route('/ads/<int:bread_id>', methods=['GET'])
@db_session
def show(work_id):
    # This will serialize our data
    schema = AdSchema()
    # This gets a work by ID
    work = Ad.get(id=work_id)

    # If we can't find a work, send a 404 response
    if not work:
        abort(404)

    # otherwise, send back the work data as JSON
    return schema.dumps(work)


@router.route('/ads/<int:work_id>', methods=['PUT'])
@db_session
@secure_route
def update(work_id):
    schema = AdSchema()
    work = Ad.get(id=work_id)

    if not work:
        abort(404)

    try:
        data = schema.load(request.get_json())
        work.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(work)


@router.route('/ads/<int:work_id>', methods=['DELETE'])
@db_session
@secure_route
def delete(work_id):
    work = Ad.get(id=work_id)

    if not work:
        abort(404)

    work.delete()
    db.commit()

    return '', 204
