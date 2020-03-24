from flask import Flask, redirect, render_template, url_for, request, session
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/")
def home():
    return render_template("Index_4+5.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.method["nm"]
        print(user)
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("Index_4+5.html")


@app.route("/user")
def user():
    if "user" in session:
        us = session["user"]
        return f"<h1>{us}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
