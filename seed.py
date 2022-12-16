from models import Pet, db

# Drop and create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

bolita = Pet(name='Bolita', species='Dog', age='2', notes='Always tries to escape', photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwuGEmugigLfQE4KqT16w9L1-0Q7cAT7XGdw&usqp=CAU')
jimmy = Pet(name='Jaimito', species='Cat', age='5', notes='Best cat ever', photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtr1smEFf1caGawkO25Oi56gGMime-wFpR2w&usqp=CAU')

db.session.add_all([bolita, jimmy])

db.session.commit()
