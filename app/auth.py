import bcrypt
from flask import Blueprint, render_template, redirect, url_for, flash
from .models import db, User
from .forms import RegisterForm

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
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

        flash("Account created.")
        return redirect(url_for("main.home"))

    return render_template("register.html", form=form)
