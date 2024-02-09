# app/catelog/routes

from app.catlog import cat


@cat.route("/catelog")
def catelog():
    return "I made it"