from flask import Flask
from flask import render_template
from flask import request
from flask import url_for, redirect
from database import *
import flask

def make_app():
    app = Flask(__name__)
    app.config.from_object('config')
    return app

app = make_app()


@app.route('/')
def hello_world():
    return render_template('index.html')
    # tested how to write functions in models lol
    # but I'm not sure whether it is the right way
    #return a

if __name__ == '__main__':
    app.run(host='0.0.0.0')
