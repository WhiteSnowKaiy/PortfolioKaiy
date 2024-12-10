from flask import Flask, render_template

root: Flask = Flask(__name__)

@root.route("/")
def index():
    return render_template("index.html")