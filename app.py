from flask import Flask, render_template, redirect, flash, session, request
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy 
from models import db, connect_db, Pet
from pets import Server_logic
###This is just to test
from forms import AddPetForm, PartialModifyPet


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_agency'
app.config['SECRET KEY'] = "There's_no_spoon"
app.config['SECRET_KEY'] = "There's_no_spoon"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

######################### Routes start here ######################

@app.route('/')
def redirect_to_users():
    """The logic needed for the function to work is at pets.py """
    all_pets = Server_logic.get_all_pets()

    return render_template('home.html', all_pets=all_pets)

@app.route('/add', methods=['POST', 'GET'])
def process_forms():
    """This will validate & process the form and then redirect to homepage"""
    
    form = Server_logic.get_pet_form()
    if form.validate_on_submit():
        Server_logic.process_add_form(form)
        return redirect('/')
    else:
        return render_template('pet-form.html', form=form)

@app.route('/<int:id>', methods=['GET', 'POST'])
def show_pet_details(id):
    """This will retrieve current pet info and send a detailed page to the user 
    that will include some fields to edit"""
    
    pet = Server_logic.get_single_pet(id)
    form = Server_logic.get_partial_form(pet)
    if form.validate_on_submit():
        Server_logic.process_edit_form(pet, form)
        return redirect('/')
    else:
        return render_template('pet-details.html', form=form, pet=pet) 






