from . import db
from datetime import datetime
from sqlalchemy import Sequence
class Reviews(db.Model):
__bind_key__ = 'db'
id = db.Column(db.Integer, Sequence('users_sequence'), unique=True,
nullable=False, primary_key=True)
user_id = db.Column(db.String(255),nullable=False)
pet_id = db.Column(db.String(255),nullable=False)
rating = db.Column(db.String(255),nullable=False)
comment = db.Column(db.String(255), nullable=False)
review_date = db.Column(db.String(255), nullable=False)
