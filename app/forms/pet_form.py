from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField
from wtforms.validators import DataRequired, ValidationError, NumberRange
from app.models import Pet
# from datetime import datetime

def petName_exists(form, field):
    name = field.data
    pet = Pet.query.filter(Pet.name == name).first()
    if pet:
        raise ValidationError('That name is already in use by another pet.')

class PetForm(FlaskForm):
    ownerId = IntegerField('ownerId')
    petTypeId = IntegerField('petTypeId', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired(), petName_exists])
    hunger = DecimalField('hunger', validators=[NumberRange(min=0, max=100)])
    description = StringField('description')