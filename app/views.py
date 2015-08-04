__author__ = 'donal'
__project__ = 'Skeletion_Flask_v11'
from app import app

@app.route('/')
def home():
    return 'Hello world of Matt'