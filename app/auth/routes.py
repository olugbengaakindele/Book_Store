# app/auth/routes
from app.auth.forms import RegistrationForm, LoginForm
from app.auth import auth
from flask import render_template, request, flash, redirect, url_for
from app.auth.models import Users

@auth.route("/register", methods= ['GET','POST'])
def register():
    name = None
    email = None
    form = RegistrationForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        Users.create_user( name ,email,  password )
        flash("You have successfully created an account with us", "info")
        return redirect(url_for("auth.login"))
    
    return render_template("reg.html", form = form , name = name , email = email , title ="Ope")


@auth.route("/login", methods= ['GET','POST'])
def login():
    name = None
    email = None
    form = LoginForm()

    return render_template("login.html", form = form , name = name , email = email)