from math import log
from flask import Blueprint, request
from flask_login import login_required, current_user
from app.forms import PetForm
from app.models import db, Pet
from .auth_routes import validation_errors_to_error_messages

pet_routes = Blueprint(('pets', __name__))

# get all pets
@pet_routes.route('/')
def all_pets():
    pets = Pet.query.all()
    return {'pets': [pet.to_dict_pet() for pet in pets]}

# get one pet based on name
@pet_routes.route('/<string:name>')
def one_pet(name):
    pet = Pet.query.get(name)
    return pet.to_dict_pet()

# create a pet
@pet_routes.route('/', methods=['POST'])
@login_required
def create_pet():
    form = PetForm()
    
    form['csrf_token'].data = request.cookies['csrf_token']
    
    # !!! TODO- if user pets.length === 4, CANNOT create pet
    currentId = current_user.get_id()
    
    if form.validate_on_submit():
        new_pet = Pet(ownerId = currentId,
                      hunger = 100)
        form.populate_obj(new_pet)
        db.session.add(new_pet)
        db.session.commit()
        return new_pet.to_dict_pet(), 201
    
    return {
        'message': 'Validation Error',
        "errors": validation_errors_to_error_messages(form.errors),
        'statusCode': 400
    }, 400

# update pet - abandon
@pet_routes.route('/<int:id>/shelter', methods=['PUT'])
@login_required
def abandon_pet(id):
    form = PetForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    
    # !!! TODO if user has no pets, CANNOT abandon anything, maybe if only 1 pet can't abandon?
    pet = Pet.query.get(id)
    
    if not pet:
        return {
            'message': 'Error',
            'errors': ['Pet couldn`t be found'],
            'statusCode': 404,
        }, 404
        
    currentId = current_user.get_id()
    if int(pet.ownerId) != int(currentId):
        return {
            'message': 'Forbidden',
            'errors': ['This pet does not belong to the current user.'],
            'statusCode': 403
        }, 403
        
    if form.validate_on_submit():
        pet.ownerId = None #none instead of 1?
        form.populate_obj(pet)
        # will need to change owner ID to 1 for paleopet 
        db.session.add(pet)
        db.session.commit()
        return pet.to_dict_project()
    
    return {
        'message': 'Validation Error',
        'errors': validation_errors_to_error_messages(form.errors),
        'statusCode': 400
    }, 400
    
# adopt pet
# if owner id is the pet shelter, then can update ownerId to current user
@pet_routes.route('/<int:id>/adopt', methods=['PUT'])
@login_required
def adopt_pet(id):
    form = PetForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    
    pet = Pet.query.get(id)
    
    if not pet:
        return {
            'message': 'Error',
            'errors': ['Pet couldn`t be found'],
            'statusCode': 404,
        }, 404
    
    # !!! TODO- if user pets.length === 4, 
                
    currentId = current_user.get_id()
    if int(pet.ownerId) != None:
        return {
            'message': 'Forbidden',
            'errors': ['This pet is not up for adoption.'],
            'statusCode': 403
        }, 403
        
    if form.validate_on_submit():
        pet.ownerId = currentId
        form.populate_obj(pet)
        # change pet owner from
        db.session.add(pet)
        db.session.commit()
        return pet.to_dict_project()
    
    return {
        'message': 'Validation Error',
        'errors': validation_errors_to_error_messages(form.errors),
        'statusCode': 400
    }, 400

# adventure? instead of over time hunger reduction
# each move reduces overall gauge, cannot continue if 0, must feed
# !!! need to set a main pet on the user, so user MUST have at least 1 pet or cannot access

#feed pet '/feed/<int:id>'
#edit to += to hunger total

#edit pet description - rich text editor