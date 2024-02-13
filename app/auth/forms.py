from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class RegistrationForm(FlaskForm):
    name = StringField("What is your name")
    email = StringField("What is your email")
    submit  = SubmitField("Register")