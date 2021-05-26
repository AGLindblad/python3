from flask import Flask, render_template, redirect, flash 

app = Flask (__name__)
app.secret_key = "ahxaefoo&fam%ei!C3Mu"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/message1")
def msgPage():
  flash("Flash forward")
  return redirect("/")

@app.route("/message2")
def msgPage2():
  flash("Flash again!")
  return redirect("/")

if __name__ == "__main__":
  app.run()
