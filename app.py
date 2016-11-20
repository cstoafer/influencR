import os

from flask import (Flask, request, session, g, redirect, url_for,
                   abort, render_template, flash)
from flask_sqlalchemy import SQLAlchemy


# create the application
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Representative


def get_state_district_by_zipcode(zipcode):
    return ('NY','1')


def get_representative_from_zipcode(zipcode):
    return {'fname': 'Cheatin\'', 'lname': 'Charlie',
            'phone': 'This isn\'t even a phone number'}


@app.route('/', methods=['GET', 'POST'])
def show_homepage():
    if request.method == 'POST':
        zipcode = request.form['zipcode']
        rep = get_representative_from_zipcode(zipcode)
        return render_template('contactinfo.html', rep=rep)
    return render_template('home.html')


@app.route('/contactinfo')
def show_contact_info():
    zipcode='2'
    rep = get_representative_from_zipcode(zipcode)
    return render_template('contactinfo.html', rep=rep)


if __name__ == '__main__':
    app.run()
