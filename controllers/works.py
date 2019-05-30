from flask import Blueprint, request, jsonify, abort, g
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Work import Work, WorkSchema
from lib.secure_route import secure_route


router = Blueprint(__name__, 'works') # creates a router for this controller

@router.route('/works', methods=['GET'])
@db_session # Allows access to the database in the `index` function
def index():
    # This will serialize our data
    # `many=True` because there are many works, ie we expect a list
    schema = WorkSchema(many=True)
    works = Work.select() # get all the works
    return schema.dumps(works) # `schema.dumps` converts the list to JSON


@router.route('/works', methods=['POST'])
@db_session
@secure_route
def create():
    # This will deserialize the JSON from insomnia
    schema = WorkSchema()

    try:
        # attempt to convert the JSON into a dict
        data = schema.load(request.get_json())
        # Use that to create a work object
        work = Work(**data, createdBy=g.current_user)
        # store it in the database
        db.commit()
    except ValidationError as err:
        # if the validation fails, send back a 422 response
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    # otherwise, send back the work data as JSON
    return schema.dumps(work), 201


@router.route('/works/<int:work_id>', methods=['GET'])
@db_session
def show(work_id):
    # This will serialize our data
    schema = WorkSchema()
    # This gets a work by ID
    work = Work.get(id=work_id)

    # If we can't find a work, send a 404 response
    if not work:
        abort(404)

    # otherwise, send back the work data as JSON
    return schema.dumps(work)


@router.route('/works/<int:work_id>', methods=['PUT'])
@db_session
@secure_route
def update(work_id):
    schema = WorkSchema()
    work = Work.get(id=work_id)

    if not work:
        abort(404)

    try:
        data = schema.load(request.get_json())
        work.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(work)


@router.route('/works/<int:work_id>', methods=['DELETE'])
@db_session
@secure_route
def delete(work_id):
    work = Work.get(id=work_id)

    if not work:
        abort(404)

    work.delete()
    db.commit()

    return '', 204
