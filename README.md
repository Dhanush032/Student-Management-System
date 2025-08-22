
# Student Management System
Django 5 + DRF + SQLite + JWT + Swagger + Bootstrap frontend (HTML/JS fetch).

Run:
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

Endpoints:
- /api/students/, /api/teachers/, /api/courses/
- JWT: /api/auth/token/
- Docs: /swagger
Frontend:
- / (home), /students/, /teachers/, /courses/, /login/
