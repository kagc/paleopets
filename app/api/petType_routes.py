from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import PetType

petType_routes = Blueprint(('petTypes', __name__))

# get all pet types
@petType_routes.route('/')
@login_required
def petTypes():
    petTypes = PetType.query.all()
    return {'petTypes': [petType.to_dict_petType() for petType in petTypes]}

#  get one pet type
@petType_routes.route('/<int:id>')
@login_required
def petTypes(id):
    petType = PetType.query.get(id)
    return petType.to_dict_petType()