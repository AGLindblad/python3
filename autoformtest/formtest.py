from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form

app = Flask(__name__)
app.secret_key = "lae0Namee0faeyo"
db = SQLAlchemy(app)

class Flower(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  type = db.Column(db.String, nullable=False)
  name = db.Column(db.String, nullable=False)

FlowerForm = model_form(Flower, base_class=FlaskForm, db_session=db.session)

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

@app.route("/new", methods=["GET", "POST"])
def addForm():
  form = FlowerForm()
  print(request.form) #test
  return render_template("new.html", form=form)

@app.route("/msg")
def msgPage():
  flash("Testmessage")
  return redirect("/")

app.run(debug=True)

