import os
import random
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import mkdtemp
from App_assist import login_required

# Configure application
app = Flask(__name__)



# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#using google spread sheet with Google spread
db = SQL("sqlite:///magic.db")

linguistics = ['Can', 'Could', 'Am', 'Are', 'Is', 'Does', 'Do',
'Did', 'Will', 'Would', 'Were', 'Was', 'Should', 'Shall', 'May',
'Might', 'Must', 'Have', 'Has']

testimony = []

@app.route("/", methods= ["GET", "POST"])
def home():
    #if request.method == "GET":
        return render_template("index.html")


@app.route("/index", methods= ["GET", "POST"])
def answer():
    if request.method == "GET":
        return render_template("index.html")
    else:
        number = random.randint(1,21)
        question = request.form.get("question")
        polar = question.split()
        if polar[0] in linguistics:

            answer = db.execute("SELECT answer FROM responces WHERE ID = :ID", ID = number)
            return render_template("reveal.html", answer=answer)

        else:
            answer = db.execute("SELECT answer FROM responces WHERE ID = :ID AND tone='neu'", ID = number)
            return render_template ("reveal.html", answer=answer)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/reviews", methods= ["GET", "POST"])
@login_required
def reviews():

    test = db.execute("""SELECT testimony FROM reviewed""")
    return render_template("reviews.html", testimony=test)


@app.route("/add", methods= ["GET", "POST"])
@login_required
def add():

    if request.method == "POST":
        testimony = request.form.get("testimony")
        db.execute("""INSERT INTO reviewed (user_ID, testimony) VALUES (:user_ID, :testimony)"""
        , user_ID= session["user_ID"], testimony= testimony)
        return render_template("reviews.html")
    else:
        return render_template("add.html")

@app.route("/reveal", methods= ["POST"] )
def reveal():
    return render_template("reveal.html")

@app.route("/login", methods= ["GET", "POST"])
def login():
    # Forget any user_ID
    session.clear()
    # User reached route via POST
    if request.method == "POST":
        # submit username
        if not request.form.get("username"):
            return error
        # submit password
        elif not request.form.get("password"):
            return error
        # query database for username
        keys = db.execute("SELECT * FROM users WHERE username = :username"
        , username = request.form.get("username"))
        # Ensure username exists and password is correct
        if len(keys) != 1 or not check_password_hash(keys[0]["hash"], request.form.get("password")):
            return error
        # log user
        session["user_ID"] = keys[0]["ID"]

        return redirect("/")
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")

@app.route("/register", methods = ["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            return error

        password = request.form.get("password")
        if not password:
            return error

        # hash of the user’s password
        hash= generate_password_hash(request.form.get("password"), method='pbkdf2:sha256')

        db.execute("""INSERT INTO users (username, hash) VALUES (:username, :hash)"""
        , username = request.form.get("username"), hash=hash)

        return redirect ("login.html")
    else:
        return render_template("register.html")
