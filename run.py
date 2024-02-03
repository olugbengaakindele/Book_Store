from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/watch")
def watch():
    movies = ["A","B","C"]
    dict_movie = {
                     "Jagujagun": 2.3,
                     "Tribe call Juda": 4.9,

                     }
    return render_template("index.html"
                           , title= "Movies"
                           , movies = movies
                           , dict_movie = dict_movie
                           
                           )






if __name__ =="__main__":
    app.run(debug = True)