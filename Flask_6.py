from flask import Flask, redirect, render_template, url_for, request, session, flash
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/")
def home():
    return render_template("Index_6.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.method["nm"]
        session["user"] = user
        flash("Login Succesful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        return render_template("Index_6.html")


@app.route("/user")
def user():
    if "user" in session:
        us = session["user"]
        return render_template("User.html", user=user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
