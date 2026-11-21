from flask import Blueprint, render_template
from flask_login import login_required
from .models import User, RepairRequest
from .roles import role_required

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/warden")
@login_required
@role_required("warden")
def warden():
    reqs = RepairRequest.query.order_by(RepairRequest.created_at.desc()).all()
    users = User.query.order_by(User.created_at.desc()).all()
    return render_template("warden.html", reqs=reqs, users=users)
