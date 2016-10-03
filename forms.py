from flask_wtf import Form 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SignupForm(Form):
  first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
  phonenumber = StringField('Phone Number', validators=[DataRequired("Please enter your phone number."), Length(min=10, message="Numbers must be atleast 10 digits.")])
  submit = SubmitField('Sign up')



