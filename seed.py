from getpass import getpass
import bcrypt
from app import create_app
from app.models import db, User

ACCOUNTS = [
    ("warden", "warden@fixey.test", "warden", None),
    ("worker1", "worker1@fixey.test", "worker", None),
    ("worker2", "worker2@fixey.test", "worker", None),
    ("student1", "student1@fixey.test", "student", "A101"),
    ("student2", "student2@fixey.test", "student", "B202"),
]

app = create_app()

password = getpass("Password for demo accounts: ")
if len(password) < 8:
    print("Password must be at least 8 characters.")
    raise SystemExit(1)

hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

with app.app_context():
    for username, email, role, room in ACCOUNTS:
        if User.query.filter_by(username=username).first():
            print(username, "already exists")
            continue

        user = User(username=username, email=email, role=role, room_number=room)
        user.password_hash = hashed
        db.session.add(user)
        print(username, "created")

    db.session.commit()
