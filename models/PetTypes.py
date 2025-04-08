from . import db
from datetime import datetime
from sqlalchemy import Sequence
class PetTypes(db.Model):
__bind_key__ = 'db'
id = db.Column(db.Integer, Sequence('users_sequence'), unique=True,
nullable=False, primary_key=True)
type_name = db.Column(db.String(255), nullable=False)
description = db.Column(db.String(255), nullable=False)
