
from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User
from forms import SignupForm
from twilio.rest import TwilioRestClient
from twilio import twiml


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/dehyusapp'
db.init_app(app)

app.secret_key = "development-key"

# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

callers = {
    "3013185581": "Curious George",
    "14103018582": "Boots",
    "+14158675311": "Virgil",
}

@app.route("/", methods=['GET', 'POST'])
def hello():
  return render_template("index.html")

@app.route("/sms", methods=['GET', 'POST'])
def sms_response():
  message_body = request.values.get('Body',None)
  resp = twiml.Response()
  if message_body == 'hello':
    resp.message('Hello ' + message_body)    
  elif message_body == 'no twili':
    resp.message('Sorry to see you go. You can always re-enroll @ twili.io :)')



  return str(resp)




   

    



@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
  ACCOUNT_SID = "AC51aa42874175a8f9a1f7b95f3a3a5fe6"
  AUTH_TOKEN = "b7fcdf5c6b0a09f106f977b58ffaadc5"
  client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
  client.messages.create(
      to="3013185581",
      from_="12407529966",
      body="Well Hello there Chelbi",
      media_url="https://media.licdn.com/mpr/mpr/shrinknp_200_200/p/2/000/188/1fc/011d373.jpg",
    )
  return "Success!"


if __name__ == "__main__":
  app.run(debug=True)