"""
Updated to allow for the config database choices.
Creation of our main tools, app and db.
Imports views for run.
"""
__author__ = 'donal'
__project__ = 'Skeletion_Flask_v11'
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # db.init_app(app)
    return app

app = create_app('development')
db = SQLAlchemy(app)
from app import views