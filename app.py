from flask import (
    Flask, redirect, render_template
)

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/search")
def about():
    return render_template("search.html")


@app.route("/create")
def contact():
    return render_template("create-recipe.html")


@app.route("/services")
def services():
    return render_template("services.html")
