from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.update(
    SECRET_KEY = 'top_secret',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:Flask123@localhost/Flaskapp',
    SQLALCHEMY_TRACK_NOTIFICATION=False
)

db = SQLAlchemy(app)

################################################################################

@app.route("/")
def home():
    return render_template("test.html")

@app.route("/watch")
def watch():
    movies = ["A","B","C"]
    dict_movie = {
                     "Jagujagun": 2.3,
                     "Tribe call Juda": 4.9,

                     }
    return render_template( "index.html" , title= "Movies" , movies = movies , dict_movie = dict_movie   )




class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def __repr__(self):
        return f"You have successfully created a new publication"
    


if __name__ =="__main__":
    db.create_all()
    app.run(debug = True)