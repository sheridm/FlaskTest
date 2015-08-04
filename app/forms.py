"""

"""
__author__ = 'donal'
__project__ = 'Skeleton_Flask_v11'

from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SubmitField, validators
from wtforms import IntegerField, RadioField, SelectField


# ----------------------------------
# LOGINS
# ----------------------------------
class SignupForm(Form):
    name = TextField("First name",  [validators.Required("Please enter your first name."),
                validators.length(max=30, message='Name too long.')])
    email = TextField("Email",  [validators.Required("Please enter your email address."),
                validators.Email("Please enter your email address."),
                validators.length(max=30, message='email too long.')])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    c_num = IntegerField('Autofilled')
    submit = SubmitField("Submit")


class sForm(Form):
    ros = RadioField('Text', choices=[], default='',)
    submit = SubmitField("Assign Line")


class baseF(Form):
    simp = SelectField('Text', choices=[('True', 'Approved'), ('False', 'NotApproved')], default='',)
    text = TextField('tex')
    submit = SubmitField("Submit")

