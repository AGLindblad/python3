from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Flower(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  type = db.Column(db.String, nullable=False)
  name = db.Column(db.String, nullable=False)

@app.before_first_request
def initMe():
  db.create_all()

  flower=Flower(type="wildflower", name="forgetmenot")
  db.session.add(flower)

  flower=Flower(type="garden flower", name="tulip")
  db.session.add(flower)

  flower=Flower(type="veggie", name="potato")
  db.session.add(flower)

  db.session.commit()

@app.route("/")
def index():
  flowers = Flower.query.all()
  return render_template("index.html", flowers = flowers)

app.run(debug=True)


