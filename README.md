# FutsalTime – Football Field Reservation API (Capstone Final)

Backend project built with **Django + Django REST Framework**.

## Features
- JWT authentication: register / login / refresh
- Fields CRUD + **availability** endpoint (hourly slots)
- Reservations: create + cancel, with **conflict prevention**
- Notifications: stored in DB, list + mark-all-read
- Swagger docs via **drf-spectacular**

## Local Setup (Windows / macOS / Linux)

### 1) Create & activate a virtual environment
**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```bat
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Run migrations + create admin user
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4) Start the server
```bash
python manage.py runserver
```

Open:
- Home page: http://127.0.0.1:8000/
- API root: http://127.0.0.1:8000/api/
- Swagger docs: http://127.0.0.1:8000/api/docs/
- Admin: http://127.0.0.1:8000/admin/

## Useful API Endpoints

### Auth
- `POST /api/auth/register/` {username, email, password}
- `POST /api/auth/login/` {username, password}
- `POST /api/auth/refresh/` {refresh}

### Fields
- `GET /api/fields/`
- `POST /api/fields/`
- `GET /api/fields/<id>/availability/?date=YYYY-MM-DD`

### Reservations
- `GET /api/reservations/`
- `POST /api/reservations/` {field, date, start_time, end_time}
- `POST /api/reservations/<id>/cancel/`

### Notifications
- `GET /api/notifications/`
- `POST /api/notifications/mark-all-read/`

## Notes
- This project uses **SQLite** by default for easy local running.
- For production you should set `DJANGO_DEBUG=0`, configure `DJANGO_ALLOWED_HOSTS`, and use a production DB.
