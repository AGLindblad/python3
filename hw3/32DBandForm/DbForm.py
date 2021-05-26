from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy #python-flask-sqlalchemy

from flask_wtf import FlaskForm #python3-flaskext.wtf
from wtforms.ext.sqlalchemy.orm import model_form

app = Flask (__name__)
app.secret_key = 'kei2shoh4xai2Zohqu0o6ahsh' 
db = SQLAlchemy(app)

class Movie(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  director = db.Column(db.String, nullable=False)

MovieForm = model_form(Movie, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initDbase():
  db.create_all()

  movie = Movie(name="Citizen Kane", director="Orson Welles")
  db.session.add(movie)

  movie = Movie(name="Battleship Potempkin", director="Sergei Eisenstein")
  db.session.add(movie)

  movie = Movie(name="Metropolis", director="Fritz Lang")
  db.session.add(movie)
  db.session.commit()

@app.route("/add")
def newMovie():
  form = MovieForm()
  return render_template("add.html", form=form)

@app.route("/")
def index():
  movies = Movie.query.all()
  return render_template("index.html", movies = movies)


if __name__ == "__main__":
  app.run(debug=True)
