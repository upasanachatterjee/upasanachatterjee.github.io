from flask import Flask
from flask import render_template
from datetime import datetime
from . import app
from hello_app.projects.tictactoe import Board

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/projects/")
def projects():
    return render_template("projects.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/projects/tic-tac-toe")
def tic_tac_toe():
    grid = Board()
    return render_template(
        "tic_tac_toe.html",
        grid=grid.board
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")