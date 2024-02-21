# app/auth/routes
from app.auth.forms import RegistrationForm, LoginForm
from app.auth import auth
from flask import render_template, request, flash, redirect, url_for
from app.auth.models import Users
from app import bcrypt
from flask_login import  login_user, logout_user,login_required, current_user


#  Home page
@auth.route("/")
def home():

    return render_template("layout.html")


# registration page
@auth.route("/register", methods= ['GET','POST'])
def register():
    if current_user.is_authenticated:
        flash("You are already logged in")
        return redirect(url_for("auth.home"))
    name = None
    email = None
    form = RegistrationForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        Users.create_user( name ,email,  password )
        flash("You have successfully created an account with us", "info")
        return redirect(url_for("auth.do_the_login"))
    
    return render_template("reg.html", form = form , name = name , email = email , title ="Ope")


@auth.route("/login", methods= ['GET','POST'])
def do_the_login():
    if current_user.is_authenticated:
        flash("You are already logged in")
        return redirect(url_for("auth.home"))
     
    name = None
    email = None
    form = LoginForm()

    if form.validate_on_submit():
        user_email = request.form['email']
        passwd = request.form['password']
        user = Users.query.filter_by(email = user_email).first()
        #  check is email exist and pasword match
        if not (user or bcrypt.check_password_hash(user.password, passwd) ):
       
            flash("Invalid credentials, please try again")
            return redirect(url_for("auth.do_the_login"))

        login_user(user,form.stayloggedin.data )
        return redirect(url_for("auth.home"))
    

    return render_template("login.html", form = form , name = name , email = email)


@auth.route("/logout")
@login_required
def logout():
    logout_user()

    return redirect(url_for("auth.home"))
