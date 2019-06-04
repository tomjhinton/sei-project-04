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
        # Use that to create a ad object
        ad = Ad(**data, createdBy=g.current_user)
        # store it in the database
        db.commit()
    except ValidationError as err:
        # if the validation fails, send back a 422 response
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    # otherwise, send back the ad data as JSON
    return schema.dumps(ad), 201


@router.route('/ads/<int:ad_id>', methods=['GET'])
@db_session
def show(ad_id):
    # This will serialize our data
    schema = AdSchema()
    # This gets a ad by ID
    ad = Ad.get(id=ad_id)

    # If we can't find a ad, send a 404 response
    if not ad:
        abort(404)

    # otherwise, send back the ad data as JSON
    return schema.dumps(ad)


@router.route('/ads/<int:ad_id>', methods=['PUT'])
@db_session
@secure_route
def update(ad_id):
    schema = AdSchema()
    ad = Ad.get(id=ad_id)

    if not ad:
        abort(404)

    try:
        data = schema.load(request.get_json())
        ad.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(ad)


@router.route('/ads/<int:ad_id>', methods=['DELETE'])
@db_session
@secure_route
def delete(ad_id):
    ad = Ad.get(id=ad_id)

    if not ad:
        abort(404)

    ad.delete()
    db.commit()

    return '', 204
