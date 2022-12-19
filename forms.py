from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    """Form for adding pets to the database"""

    name = StringField('Pet name', validators=[InputRequired(message="Pet name cannot be blank")])
    species = SelectField('Species', validators=[InputRequired(message="Species fiels cannot be blank")], choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porc', 'Porcupine')])
    photo_url = StringField('Photo URL', validators=[Optional(), URL(require_tld=True, message='Please provide a valid URL address or leave the field empty')] )
    age = FloatField('Age', validators=[Optional(), NumberRange(min=0, max=30, message='The age of the pet must be between %(min)s and %(max)s years')])
    notes = StringField('Notes', validators=[Optional()])
    available = available = BooleanField('Available', validators=[Optional()])

class PartialModifyPet(FlaskForm):
    """This will have less arguments to modify an existing pet"""
    
    photo_url = StringField('Photo URL', validators=[Optional(), URL(require_tld=True, message='Please provide a valid URL address or leave the field empty')])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField('Available')
