from flask import Flask , jsonify , request
import csv

all_movies = []

with open("movies.csv" ,encoding = "utf-8") as f:
    r = csv.reader(f)
    data = list(r)
    all_movies = data[1:]

like_movies = []
not_like_movies = []
did_not_watch = []

app = Flask(__name__)

@app.route("/")
def home():
    return "welcome to home page"

@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data" : all_movies[0],
        "status" : "success"
    })

@app.route("/liked-movie", methods = ["POST"])
def liked_movie():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    like_movies.append(movie)
    return jsonify({
        "status" : "success",
    }),200

@app.route("/unliked-movie" , methods = ["POST"])
def unliked_movie():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_like_movies.append(movie)
    return jsonify({
        "status" : "success"
    }),200

@app.route("/did-not-watch" , methods = ["POST"])
def did_not_watch():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch.append(movie)
    return jsonify({
        "status" : "success"
    }),200


if __name__ == "__main__":
    app.run(debug = True)
