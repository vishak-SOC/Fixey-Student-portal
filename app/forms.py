import re
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import SelectField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo, ValidationError


def strong_password(form, field):
    password = field.data
    if not re.search(r"[A-Z]", password):
        raise ValidationError("Needs an uppercase letter.")
    if not re.search(r"[a-z]", password):
        raise ValidationError("Needs a lowercase letter.")
    if not re.search(r"[0-9]", password):
        raise ValidationError("Needs a number.")


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[
        DataRequired(),
        Length(min=3, max=30),
        Regexp(r"^[A-Za-z0-9_]+$", message="Letters, numbers and _ only."),
    ])
    email = StringField("Email", validators=[
        DataRequired(),
        Length(max=120),
        Regexp(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", message="Enter a valid email."),
    ])
    room_number = StringField("Room number", validators=[
        DataRequired(),
        Length(max=10),
        Regexp(r"^[A-Za-z0-9-]+$", message="Letters and numbers only."),
    ])
    password = PasswordField("Password", validators=[
        DataRequired(),
        Length(min=8, max=64),
        strong_password,
    ])
    confirm = PasswordField("Confirm password", validators=[
        DataRequired(),
        EqualTo("password", message="Passwords do not match."),
    ])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(max=30)])
    password = PasswordField("Password", validators=[DataRequired(), Length(max=64)])
    submit = SubmitField("Login")


CATEGORIES = ["Heating", "Plumbing", "Electrical", "Wi-Fi", "Furniture", "Other"]


class RequestForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=3, max=100)])
    category = SelectField("Category", choices=CATEGORIES)
    description = TextAreaField("Description", validators=[
        DataRequired(),
        Length(min=10, max=1000),
    ])
    entry_permission = BooleanField("Staff can enter my room if I am not there")
    submit = SubmitField("Send request")
