from flask import (
    Flask,
    render_template,
    request,
    make_response,
    redirect,
    url_for,
    session,
)
import secrets
from forms import RegistrationForm
from models import db, User
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_hex()
csrf = CSRFProtect(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db.init_app(app)


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


@app.route("/registration/", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("registration.html", title="Регистрация", form=form)


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


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("Initialized the database")


if __name__ == "__main__":
    app.run(debug=True)
