# Fixey - Student Accommodation Repair Portal

Fixey is a web app for reporting repairs in student accommodation. Students report a problem in their room, the warden sets a priority and assigns it to a worker, and the worker updates the job until it is fixed.

Made for the Secure Web Development module (MSc Cybersecurity, NCI). Requests hold private details like room numbers and entry permission, so only the right people should see them.

**Still in progress.**

## Planned features

**Students**
- Register and log in
- Create, view, edit and cancel their own requests
- Comment on their own requests

**Maintenance workers**
- See only jobs assigned to them
- Update job status and add comments

**Warden (admin)**
- See all requests, set priority and assign workers
- Create worker accounts
- View the audit log

## Planned security features

| # | Area | Plan |
|---|---|---|
| 1 | Authentication | bcrypt hashing, password rules, lockout after failed logins |
| 2 | Authorization | Roles (student / worker / warden), users only see their own requests or jobs |
| 3 | Privacy | Room number and entry details hidden from others |
| 4 | Sessions | Secure, HttpOnly, SameSite cookies and session timeout |
| 5 | SQL injection | Form validation and ORM queries only |
| 6 | XSS and CSRF | Escaped output and CSRF tokens on forms |
| 7 | Headers | CSP, X-Frame-Options and other headers |
| 8 | Logging and errors | Audit log and custom error pages |

## Tech stack

- Python 3, Flask
- SQLite (Flask-SQLAlchemy)
- HTML, Jinja, CSS

## Setup

You need Python 3 and Git.

1. Clone the repo
   ```bash
   git clone https://github.com/vishak-SOC/Fixey-Student-portal.git
   cd Fixey-Student-portal
   ```

2. Create a virtual environment and install packages
   ```bash
   python3 -m venv venv
   venv/bin/pip install -r requirements.txt
   ```
   On Windows use `venv\Scripts\pip`.

3. Create the `.env` file
   ```bash
   cp .env.example .env
   ```

4. Make a secret key and put it in `.env` instead of `change-me`
   ```bash
   python3 -c "import secrets; print(secrets.token_hex(32))"
   ```

5. Run the app
   ```bash
   venv/bin/python run.py
   ```
   Open http://127.0.0.1:5000

On Mac, use `127.0.0.1` not `localhost` (AirPlay uses port 5000).

## Author

Vishak Siva Narayanan Priya - MSc Cybersecurity, NCI
