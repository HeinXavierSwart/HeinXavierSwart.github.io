from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")

# This ensures URLs generated by Flask-Freeze will have the right path
@app.route('/index.html')
def index_html():
    return index()

