from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User
from forms import SignupForm
from twilio.rest import TwilioRestClient
from twilio import twiml
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:deahware1@localhost/dehyusapp'
db.init_app(app)

app.secret_key = "development-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
  form = SignupForm()
  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser= User(form.phonenumber.data)
      db.session.add(newuser)
      db.session.commit()

      session['phonenumber'] = newuser.phonenumber
      return redirect(url_for('success'))

  elif request.method == "GET":
    return render_template('signup.html', form=form)

@app.route("/success")
def success():
  return render_template("success.html")

@app.route("/sms", methods=['GET', 'POST'])
def sms_response():
  message_body = request.values.get('Body',None)
  resp = twiml.Response()
  if message_body == 'hello':
    resp.message('Hello ' + message_body)    
  elif message_body == 'no twili':
    resp.message('Sorry to see you go. You can always re-enroll @ twili.io :)')
  else:
    resp.message('mmhmm ')

  return str(resp)




if __name__ == "__main__":
  app.run(debug=True)