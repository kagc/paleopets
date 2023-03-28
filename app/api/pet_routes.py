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