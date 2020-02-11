import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()
# We would change the ENV variable during development and production
ENV = 'dev'


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
#No create all will be required, as we're using flask_migrate

class Drink(db.Model):
    __tablename__ = 'Drink'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    tagline =  db.Column(db.String(180), nullable=False)

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'tagline': self.tagline
        }


    def insert(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
