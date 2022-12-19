from models import Pet, db, connect_db
from forms import AddPetForm, PartialModifyPet


class Server_logic():
    """This will provide extra functionality to process flask app.py and WTForms with the Pet model """
    
    @staticmethod
    def get_all_pets():
        return Pet.query.all()
    
    @staticmethod
    def get_single_pet(id):
        return Pet.query.get_or_404(id)

    @staticmethod
    def get_pet_form():
        return AddPetForm()
    
    @staticmethod
    def process_add_form(form):
        """This will create a new pet from WTForms using the Pet model"""
        
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        db.session.add(
            Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes))
        db.session.commit()
    
    @staticmethod
    def get_partial_form(pet_obj):
        return PartialModifyPet(obj=pet_obj)

    @staticmethod
    def process_edit_form(pet, form):
        """This will update the fields on the Pet model"""
        
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        





    
        
        
        

    
        
    
            
            

        



        