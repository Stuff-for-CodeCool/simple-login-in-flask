from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = "askfuasdkvaksjfakjsdf"

users = {"alex": "1234", "laura": "2468", "cipi": "1357"}


@app.route("/")
def index():
    user = session.get("user")
    return render_template("index.html", user=user)


@app.route("/register", methods=["GET", "POST"])
def register():
    global users

    if request.method == "POST":
        users[request.form.get("user")] = request.form.get("pass")
        session["user"] = request.form.get("user")

        return redirect(url_for("index"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    global users

    if request.method == "POST":
        u = request.form.get("user")
        p = request.form.get("pass")

        if u in users.keys() and users[u] == p:
            session["user"] = u

        return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
