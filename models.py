from flask.ext.sqlalchemy import SQLAlchemy


import geocoder
from urllib.request import urlopen
import json


db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  phonenumber = db.Column(db.String(120), unique=True)
  

  def __init__(self, phonenumber):
    self.phonenumber = phonenumber.lower()
    
     
  