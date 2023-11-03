

from flask import Flask, url_for, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route("/<name>")
def hello_world(name):
    return f"<p>Hello, {escape(name)}!</p>"
