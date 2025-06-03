# UserAuthWeb

A web application for user authentication, featuring registration, login, and profile management.

- **Frontend**: HTML + Tailwind CSS (via CDN)  
- **Backend**: Django REST Framework with JWT Authentication (`rest_framework_simplejwt`)  
- **Features**:
  - User Registration & Login
  - JWT Token Authentication
  - Profile Management
  - Field-level error validation
  - Auto-dismissable Notifications
  - Page Redirects on Auth Events

---

## 🚀 Features

- **User Registration**: Create account with `username`, `email`, and `password`.
- **User Login**: Authenticate via `email` and `password`, receive JWT tokens.
- **Profile Page**: View and update `username` and `email`.
- **Notifications**: Success/Error messages appear in top-right corner (auto-hide in 5s).
- **Secure Auth**: Token-based via `rest_framework_simplejwt`.
- **Validation**: Field-specific errors shown below form inputs.
- **Redirects**: Auto-redirect after registration/login to next page.

---

## 🔧 Prerequisites

- Python 3.8+
- pip
- Git
- (Optional) Node.js — for Tailwind customization
- A Web Browser (e.g. Chrome, Firefox)

---

## ⚙️ Installation

### 📦 Backend Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/userauthweb.git
    cd userauthweb
    ```

2. **Create Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate        # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Django Settings**:  
   Edit `backend/settings.py`:

    ```python
    INSTALLED_APPS = [
        ...
        'rest_framework',
        'corsheaders',
        'yourapp',  # Replace with your Django app name
    ]

    MIDDLEWARE = [
        ...
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        ...
    ]

    CORS_ALLOWED_ORIGINS = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ],
    }
    ```

5. **Run Migrations**:
    ```bash
    python backend/manage.py makemigrations
    python backend/manage.py migrate
    ```

6. **Create Superuser (optional)**:
    ```bash
    python backend/manage.py createsuperuser
    ```

7. **Run Development Server**:
    ```bash
    python backend/manage.py runserver
    ```

Backend running at: `http://127.0.0.1:8000`

---

### 🎨 Frontend Setup

1. **Place Frontend Files**:  
   Ensure `register.html`, `login.html`, and `profile.html` are in the root folder or `frontend/` directory.

2. **Run Local Web Server**:
    ```bash
    python -m http.server 3000
    ```

3. **Access App**:
    - Registration: `http://localhost:3000/register/`
    - Login: `http://localhost:3000/login/`
    - Profile: `http://localhost:3000/profile/`

---

## 📄 API Endpoints

All endpoints are under: `http://127.0.0.1:8000/api/auth/`

| Endpoint            | Method | Description             | Request Body Example                                     | Response Example                             |
|---------------------|--------|-------------------------|----------------------------------------------------------|----------------------------------------------|
| `/register/`        | POST   | Register a new user     | `{"username": "user", "email": "email", "password": "pass"}` | `{"detail": "Registration successful"}`     |
| `/login/`           | POST   | Authenticate user       | `{"email": "email", "password": "pass"}`                    | `{"access": "...", "refresh": "..."}`        |
| `/dashboard/`       | GET    | Get current user data   | (Requires `Authorization: Bearer <access_token>`)          | `{"username": "...", "email": "..."}`        |
| `/user/{username}/` | PATCH  | Update user profile     | `{"username": "new", "email": "new@example.com"}`          | `{"username": "...", "email": "..."}`        |

---

## 🔐 Authentication

- Use JWT tokens from `/login/`.
- Send `Authorization: Bearer <access_token>` for protected routes.

---

## 📁 File Structure


---

## 🧪 Testing

### ✅ Backend

- Run Django tests:
    ```bash
    python backend/manage.py test
    ```

- Test endpoints using `curl`:
    ```bash
    curl -X POST http://127.0.0.1:8000/api/auth/register/ \
    -H "Content-Type: application/json" \
    -d '{"username": "testuser", "email": "test@example.com", "password": "password123"}'
    ```

### ✅ Frontend

- Visit `http://localhost:3000/register/` and test full auth flow:
  - Register ➜ Login ➜ Profile
  - Edit profile ➜ Save/Cancel ➜ Logout
- Ensure:
  - Field-level validation errors show up correctly.
  - Toast notifications appear/disappear after 5 seconds.

---

## 📌 Notes

- Tailwind CSS is included via CDN in the HTML files:
    ```html
    <script src="https://cdn.tailwindcss.com"></script>
    ```
- For customization, install Tailwind CLI and generate config.

---

## 📬 License

MIT — use freely for personal or commercial projects.
