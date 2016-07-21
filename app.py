import os

from flask import Flask
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

if os.environ.get('FLASK_ENV', "production") == "development":
    print "In development mode"
    app.config['DEBUG'] = True

    print app.config['DEBUG']

@app.route("/")
def index():
    return "Hello world"
