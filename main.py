import os

import sqlite3
from flask import (Flask, request, session, g, redirect, url_for,
                   abort, render_template, flash)
from contextlib import closing

# configuration
DATABASE = 'data/db.db'
DEBUG = True
SECRET_KEY = 'development key'

# create the application
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def show_homepage():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
