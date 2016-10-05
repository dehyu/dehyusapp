from flask_wtf import Form 
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, Length

class SignupForm(Form):
  phonenumber = StringField('Please enter your phone number', validators=[DataRequired("Please enter your phone number."), Length(min=10, message="Numbers must be 10 digit lenght, at minimum")])
  submit = SubmitField('Sign up')

