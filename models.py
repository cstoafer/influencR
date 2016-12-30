from app import db
from sqlalchemy.dialects.postgresql import JSON


class Representative(db.Model):
    __tablename__ = 'representatives'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    state = db.Column(db.String())
    district = db.Column(db.String())
    phone = db.Column(db.String())

    def __init__(self, first_name, last_name, state, district, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.state = state
        self.district = district
        self.phone = phone

    def __repr__(self):
        return '<id {}>'.format(self.id)
