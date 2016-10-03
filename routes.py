from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User
from forms import SignupForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/dehyusapp'
db.init_app(app)

app.secret_key = "development-key"

@app.route("/", methods=['GET', 'POST'])
def index():
  return render_template("index.html")
  resp = twilio.twiml.Response()
  resp.message("Hello, Mobile Monkey")
  return str(resp)

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if 'phonenumber' in session:
    return redirect(url_for('home'))

  form = SignupForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      resp = twilio.twiml.Response()
      resp.message("Hello, Mobile Monkey")
      return str(resp)

  return 'Success'




@app.route("/login", methods=["GET", "POST"])
def login():
  if 'phonenumber' in session:
    return redirect(url_for('home'))

  form = LoginForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template("login.html", form=form)
    else:
      phonenumber = form.phonenumber.data 
      password = form.password.data 

      user = User.query.filter_by(phonenumber=phonenumber).first()
      if user is not None and user.check_password(password):
        session['phonenumber'] = form.phonenumber.data 
        return redirect(url_for('home'))
      else:
        return redirect(url_for('login'))

  elif request.method == 'GET':
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
  session.pop('phonenumber', None)
  return redirect(url_for('index'))

if __name__ == "__main__":
  app.run(debug=True)