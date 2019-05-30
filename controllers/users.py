from flask import Blueprint, request, jsonify, abort
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.User import User, UserSchema
from lib.secure_route import secure_route


router = Blueprint(__name__, 'users') # creates a router for this controller

@router.route('/users', methods=['GET'])
@db_session # Allows access to the database in the `index` function
def index():
    # This will serialize our data
    # `many=True` because there are many users, ie we expect a list
    schema = UserSchema(many=True)
    users = User.select() # get all the users
    return schema.dumps(users) # `schema.dumps` converts the list to JSON


@router.route('/users', methods=['POST'])
@db_session
@secure_route
def create():
    # This will deserialize the JSON from insomnia
    schema = UserSchema()

    try:
        # attempt to convert the JSON into a dict
        data = schema.load(request.get_json())
        # Use that to create a user object
        user = User(**data)
        # store it in the database
        db.commit()
    except ValidationError as err:
        # if the validation fails, send back a 422 response
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    # otherwise, send back the user data as JSON
    return schema.dumps(user), 201


@router.route('/users/<int:user_id>', methods=['GET'])
@db_session
def show(user_id):
    # This will serialize our data
    schema = UserSchema()
    # This gets a user by ID
    user = User.get(id=user_id)

    # If we can't find a user, send a 404 response
    if not user:
        abort(404)

    # otherwise, send back the user data as JSON
    return schema.dumps(user)


@router.route('/users/<int:user_id>', methods=['PUT'])
@db_session
@secure_route
def update(user_id):
    schema = UserSchema()
    user = User.get(id=user_id)

    if not user:
        abort(404)

    try:
        data = schema.load(request.get_json())
        user.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(user)


@router.route('/users/<int:user_id>', methods=['DELETE'])
@db_session
@secure_route
def delete(user_id):
    user = User.get(id=user_id)

    if not user:
        abort(404)

    user.delete()
    db.commit()

    return '', 204
