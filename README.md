# FutsalTime Backend

Django + Django REST Framework backend for a futsal field reservation system.

## Setup

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver
```

## Main API Endpoints (starter)

- `POST /api/auth/register/`
- `POST /api/auth/login/`
- `POST /api/auth/refresh/`
- `GET  /api/users/profile/`
- `PUT  /api/users/profile/`
- `GET  /api/users/booking-history/`
- `GET  /api/fields/`
- `GET  /api/fields/<id>/`
- `GET  /api/reservations/available-slots/?date=YYYY-MM-DD&field=1`
- `POST /api/reservations/`
- `GET  /api/reservations/my-reservations/`
- `GET  /api/reservations/<id>/`
- `PUT  /api/reservations/<id>/cancel/`
- `GET  /api/notifications/`
- `PUT  /api/notifications/<id>/mark-read/`
- `GET  /api/notifications/unread-count/`
```

Use this as a starting point and extend business logic, validations, and admin endpoints as you progress through the capstone.
