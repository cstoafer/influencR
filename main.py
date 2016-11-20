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

def get_state_district_by_zipcode(zipcode):
    return ('NY','1')

def get_representative_from_zipcode(zipcode):
    state, district = get_state_district_by_zipcode(zipcode)
    query = ('SELECT first_name, last_name, phone '
             'FROM representatives '
             'WHERE state = "{}" AND district = "{}";'.format(state,district))
    cur = g.db.execute(query)
    rep_rows = cur.fetchall()
    if len(rep_rows) == 0:
        raise ValueError('representative not found for zipcode')
    assert(len(rep_rows) == 1)
    rep_row = rep_rows[0]
    rep = dict(fname=rep_row[0], lname=rep_row[1], phone=rep_row[2])
    return rep

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET', 'POST'])
def show_homepage():
    rep = None
    if request.method == 'POST':
        zipcode = request.form['zipcode']
        rep = get_representative_from_zipcode(zipcode)
        #return render_template('contactinfo.html', rep=rep)
    return render_template('home.html', rep=rep)

@app.route('/contactinfo')
def show_contact_info():
    zipcode='2'
    rep = get_representative_from_zipcode(zipcode)
    return render_template('contactinfo.html', rep=rep)


if __name__ == '__main__':
    app.run()
