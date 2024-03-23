from flask import Flask, render_template, request, make_response, redirect, url_for, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/auth/", methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        session["name"] = name
        session["email"] = email

        return redirect(url_for("welcome"))

    return render_template("auth.html")


@app.route("/welcome/")
def welcome():
    name = session.get("name", "Guest")
    email = session.get("email", "")
    return render_template("welcome.html", name=name, email=email)


@app.route("/logout/")
def logout():
    session.clear()
    return redirect(url_for("auth"))


@app.route("/cpu/")
def cpu():
    return render_template("cpu.html")


@app.route("/memory/")
def memory():
    return render_template("memory.html")


@app.route("/motherboard/")
def motherboard():
    return render_template("motherboard.html")


if __name__ == "__main__":
    app.run(debug=True)
