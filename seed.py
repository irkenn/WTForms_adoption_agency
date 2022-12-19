from models import Pet, db

"""Drop and create all tables"""
db.drop_all()
db.create_all()

"""If the table isn't empty, empty it"""
Pet.query.delete()

"""Create model instances"""
bolita = Pet(name='Bolita', species='Dog', age='2', notes='Always tries to escape', photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwuGEmugigLfQE4KqT16w9L1-0Q7cAT7XGdw&usqp=CAU')
jimmy = Pet(name='Jaimito', species='Cat', age='5', notes='Best cat ever', photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtr1smEFf1caGawkO25Oi56gGMime-wFpR2w&usqp=CAU')
walrus = Pet(name='Walrus', species='Walrus', age='15', notes='Eats lots of fish, lots!', photo_url='https://i.natgeofe.com/n/2001a813-50b9-4f1f-8557-c8736df9d2e4/walrus_thumb.JPG', available=False)


"""Add and commit"""
db.session.add_all([bolita, jimmy, walrus])
db.session.commit()



