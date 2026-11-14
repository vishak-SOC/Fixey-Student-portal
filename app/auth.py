import bcrypt
from flask import Blueprint, render_template, redirect, url_for, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from .models import db, User
from .forms import RegisterForm, LoginForm

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data.strip()
        email = form.email.data.strip().lower()

        existing = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing:
            flash("Username or email already used.")
            return render_template("register.html", form=form)

        hashed = bcrypt.hashpw(form.password.data.encode(), bcrypt.gensalt())

        user = User(
            username=username,
            email=email,
            room_number=form.room_number.data.strip().upper(),
            password_hash=hashed.decode(),
            role="student",
        )
        db.session.add(user)
        db.session.commit()

        flash("Account created. Please log in.")
        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data.strip()).first()

        if user and user.is_active and bcrypt.checkpw(form.password.data.encode(), user.password_hash.encode()):
            session.clear()
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("main.home"))

        flash("Wrong username or password.")

    return render_template("login.html", form=form)


@auth.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    session.clear()
    flash("Logged out.")
    return redirect(url_for("auth.login"))
