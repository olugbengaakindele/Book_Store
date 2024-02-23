from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,EmailField, BooleanField
from wtforms.validators import DataRequired,Email,Length,ValidationError
from app.auth.models import Users


def email_check_for_reg(form,field):
    user = Users.query.filter_by(email = field.data).first()
    if user :
        raise ValidationError("Email exist, please login into your account") 


def email_check_for_login(form,field):
    user = Users.query.filter_by(email = field.data).first()
    if not user :
        raise ValidationError("Invalid credentials, please check that email and password are correct") 

class RegistrationForm(FlaskForm):
    name = StringField("What is your name")
    email = EmailField("What is your email", validators=[DataRequired(), Length(5,100),Email(),email_check_for_reg])
    password = PasswordField("Enter a password", validators=[Length(5,20, message="must be 5 to 20 chracters")])
    submit  = SubmitField("Register")


class LoginForm(FlaskForm):
    email = EmailField("What is your email", validators=[DataRequired(), Length(5,100),email_check_for_login])
    password = PasswordField("Enter a password")
    stayloggedin = BooleanField("stay logged in?")
    submit  = SubmitField("Login")


class PublisherForm(FlaskForm):
    name = StringField("Publisher Name", validators=[DataRequired(), Length(5,100)])
    submit  = SubmitField("Submit")