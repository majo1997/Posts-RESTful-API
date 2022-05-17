import os
from os import environ
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from application import app

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Config:
    #HOST = environ.get('FLASK_RUN_HOST')
    #PORT = environ.get('FLASK_RUN_PORT')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db/db.sqlite'#os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    EXTERNAL_REST_URL = environ.get('EXTERNAL_REST_URL')
