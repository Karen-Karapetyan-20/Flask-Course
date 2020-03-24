from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("Index_3.html", content="Testing")

@app.route("/test")
def test():
    return render_template("New.html", content="Testing")

if __name__ == "__main__":
    app.run(debug=True)
