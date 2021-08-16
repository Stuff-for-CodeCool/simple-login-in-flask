from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register")
def register():
    pass


@app.route("/login")
def login():
    pass


@app.route("/logout")
def logout():
    pass


if __name__ == "__main__":
    app.run(debug=True)
