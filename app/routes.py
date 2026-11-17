from flask import Blueprint, render_template
from flask_login import login_required
from .models import User
from .roles import role_required

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/warden")
@login_required
@role_required("warden")
def warden():
    users = User.query.order_by(User.created_at.desc()).all()
    return render_template("warden.html", users=users)
