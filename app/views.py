__author__ = 'donal'
__project__ = 'Skeletion_Flask_v11'
from app import app
from flask import render_template, request, flash, session, url_for, redirect
from forms import SigninForm, SignupForm

@app.route('/')
def home():
    return 'Hello world of Matt'