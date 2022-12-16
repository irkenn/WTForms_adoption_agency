from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)


class Pet(db.Model):
    """This is the user model"""
    __tablename__ = 'pets'

    def __repr__(self):
        p = self
        return f"<Pet id={p.id} name={p.name} species={p.species} age={p.age} available={p.available}>"

    id =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text,  nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default=True)




