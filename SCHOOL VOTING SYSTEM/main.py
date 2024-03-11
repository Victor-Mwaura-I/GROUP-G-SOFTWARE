from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def register():
  form=RegistrationForm()
  return render_template("registration.html", title=Register, form=form)


@app.route("/register")
def register():
  form=LoginForm()
  return render_template("login.html", title=Login, form=form)

if __name__ == "__main__":
   app.run()
