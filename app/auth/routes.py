# app/auth/routes
from app.auth.forms import RegistrationForm
from app.auth import auth
from flask import render_template


@auth.route("/register")
def register():
    form = RegistrationForm()

    return render_template("reg.html", form = form)