# Fixey – Student Accommodation Repair Portal

Fixey is a small web app for student accommodation. When something breaks in a student's room (a heater, the Wi-Fi, a leaking tap), the student logs a repair request. The warden looks at new requests, sets a priority and assigns them to a maintenance worker. The worker then updates the job until it is fixed.

I'm building it for the **Secure Web Development** module (MSc in Cybersecurity, National College of Ireland). The main focus is security: every request holds private details such as a student's room number and when someone is allowed to enter the room, so the app must only show that to the people who really need it.

> 🚧 **Work in progress.** This README will be updated as each feature is added.

## Planned features

**Students**
- Register and log in
- Create, view, edit and cancel their own repair requests
- Add comments to their own requests

**Maintenance workers**
- See only the jobs assigned to them
- Update the job status (In progress → Fixed) and add comments

**Warden (admin)**
- See all requests, set priority, assign jobs to workers
- Create worker accounts and manage user roles
- View the audit log

## Planned security features

| # | Area | What is planned |
|---|---|---|
| 1 | Authentication | Hashed passwords (bcrypt), password rules, account lockout after repeated failed logins |
| 2 | Authorization | Role-based access (student / worker / warden), checks that users only open their own requests or assigned jobs |
| 3 | Privacy | Room number and entry times hidden from anyone who doesn't need them |
| 4 | Sessions | Secure, HttpOnly and SameSite cookies with a session timeout |
| 5 | Input validation and SQL injection | Form validation and ORM queries only (no SQL built from strings) |
| 6 | XSS and CSRF | Escaped output in templates and a CSRF token on every form |
| 7 | Security headers | Content Security Policy, anti-clickjacking and other headers |
| 8 | Logging and errors | Audit log of important actions and custom error pages that don't leak details |

## Tech stack

- Python 3 and Flask
- SQLite (through Flask-SQLAlchemy)
- HTML, Jinja templates and CSS

## Setup and installation

You need **Python 3** and **Git** installed.

1. Clone the repository and go into the folder:
   ```bash
   git clone https://github.com/vishak-SOC/Fixey-Student-portal.git
   cd Fixey-Student-portal
   ```

2. Create a virtual environment and install the packages:
   ```bash
   python3 -m venv venv
   venv/bin/pip install -r requirements.txt
   ```
   (On Windows use `venv\Scripts\pip` instead of `venv/bin/pip`.)

3. Create your own `.env` file from the example:
   ```bash
   cp .env.example .env
   ```

4. Make a secret key and paste it into `.env` in place of `change-me`:
   ```bash
   python3 -c "import secrets; print(secrets.token_hex(32))"
   ```
   The app will not start if the key is missing or still set to `change-me`.

5. Run the app:
   ```bash
   venv/bin/python run.py
   ```
   Then open **http://127.0.0.1:5000** in your browser. Press `Ctrl + C` to stop it.

> **Mac users:** if the page doesn't load, AirPlay Receiver might be using port 5000. Use `127.0.0.1` instead of `localhost`, or turn AirPlay Receiver off in System Settings.

## Author

Vishak Siva Narayanan Priya – MSc in Cybersecurity, National College of Ireland
