from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

import geocoder
import urllib.request
import json


db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  phonenumber = db.Column(db.String(100))
 

  def __init__(self, firstname, phonenumber):
    self.firstname = firstname.title()
    self.phonenumber = phonenumber.title()
    
     
  
