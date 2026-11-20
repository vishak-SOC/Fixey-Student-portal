from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from .models import db, RepairRequest, Comment
from .forms import RequestForm, CommentForm
from .roles import role_required

repairs = Blueprint("repairs", __name__)


def can_view(req):
    if current_user.role == "warden":
        return True
    if current_user.role == "worker":
        return req.worker_id == current_user.id
    return req.student_id == current_user.id


@repairs.route("/requests")
@login_required
@role_required("student")
def my_requests():
    reqs = RepairRequest.query.filter_by(student_id=current_user.id)
    reqs = reqs.order_by(RepairRequest.created_at.desc()).all()
    return render_template("requests.html", reqs=reqs)


@repairs.route("/requests/new", methods=["GET", "POST"])
@login_required
@role_required("student")
def new_request():
    form = RequestForm()

    if form.validate_on_submit():
        req = RepairRequest(
            title=form.title.data.strip(),
            category=form.category.data,
            description=form.description.data.strip(),
            room_number=current_user.room_number,
            entry_permission=form.entry_permission.data,
            student_id=current_user.id,
        )
        db.session.add(req)
        db.session.commit()

        flash("Request sent.")
        return redirect(url_for("repairs.view_request", id=req.id))

    return render_template("request_new.html", form=form)


@repairs.route("/requests/<int:id>")
@login_required
def view_request(id):
    req = db.get_or_404(RepairRequest, id)

    if not can_view(req):
        abort(403)

    return render_template("request_view.html", req=req, form=CommentForm())


def get_own_new_request(id):
    req = db.get_or_404(RepairRequest, id)

    if req.student_id != current_user.id:
        abort(403)
    if req.status != "new":
        flash("This request can no longer be changed.")
        return None

    return req


@repairs.route("/requests/<int:id>/edit", methods=["GET", "POST"])
@login_required
@role_required("student")
def edit_request(id):
    req = get_own_new_request(id)
    if req is None:
        return redirect(url_for("repairs.view_request", id=id))

    form = RequestForm(obj=req)

    if form.validate_on_submit():
        req.title = form.title.data.strip()
        req.category = form.category.data
        req.description = form.description.data.strip()
        req.entry_permission = form.entry_permission.data
        db.session.commit()

        flash("Request updated.")
        return redirect(url_for("repairs.view_request", id=req.id))

    return render_template("request_edit.html", form=form, req=req)


@repairs.route("/requests/<int:id>/cancel", methods=["POST"])
@login_required
@role_required("student")
def cancel_request(id):
    req = get_own_new_request(id)
    if req is None:
        return redirect(url_for("repairs.view_request", id=id))

    req.status = "cancelled"
    db.session.commit()

    flash("Request cancelled.")
    return redirect(url_for("repairs.my_requests"))


@repairs.route("/requests/<int:id>/comment", methods=["POST"])
@login_required
def add_comment(id):
    req = db.get_or_404(RepairRequest, id)

    if not can_view(req):
        abort(403)
    if req.status == "cancelled":
        flash("This request is cancelled.")
        return redirect(url_for("repairs.view_request", id=id))

    form = CommentForm()

    if form.validate_on_submit():
        comment = Comment(request_id=req.id, author_id=current_user.id, text=form.text.data.strip())
        db.session.add(comment)
        db.session.commit()
        flash("Comment added.")
    else:
        flash("Comment must be 1 to 500 characters.")

    return redirect(url_for("repairs.view_request", id=id))
