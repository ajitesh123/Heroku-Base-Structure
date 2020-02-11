import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()
# We would change the ENV variable during development and production
ENV = 'prod'


def setup_db(app, ENV=ENV):
    '''Binds a flask application and a SQLAlchemy service'''
    if ENV == 'dev':
        app.debug = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ajitesh@localhost:5432/mockdb'
    else:
        app.debug = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bsmfjjpvmspejy:8037411620a3fed176d4f8843eb2a308fac61d07863277e73d45dacc7df96a97@ec2-35-168-54-239.compute-1.amazonaws.com:5432/d3d5h5hckmgn9d'

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app

    db.init_app(app)

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

'''
Drink
a persistent drink entity, extends the base SQLAlchemy Model
'''
class Drink(db.Model):
    __tablename__ = 'Drink'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    recipe =  db.Column(db.String(180), nullable=False)
    price = db.Column(db.Integer)


    def short(self):
        print(json.loads(self.recipe))
        new_dict = {}
        for key in json.loads(self.recipe):
            if key == 'color':
                new_dict['color'] = json.loads(self.recipe)[key]
            elif key == 'parts':
                new_dict['parts'] = json.loads(self.recipe)[key]

        short_recipe = [new_dict]

        return {
            'id': self.id,
            'title': self.title,
            'recipe': short_recipe
        }


    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'recipe': json.loads(self.recipe)
        }


    def insert(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())
