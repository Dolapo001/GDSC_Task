# **User Onboarding and Profile Management Backend**

This project is a backend system built with Django and Django REST Framework (DRF) for user authentication, onboarding, and profile management. The backend is scalable, secure, and implements JWT-based authentication, OAuth2 social logins (Google and Apple), and user profile management with work experience and skills onboarding modules.

---
## **Table of Contents**

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Running the Application](#running-the-application)
6. [Environment Variables](#environment-variables)
7. [Database Setup](#database-setup)
8. [API Endpoints](#api-endpoints)
9. [Testing](#testing)
10. [API Documentation](#api-documentation)
11. [Database Schema](#database-schema)
12. [Contributing](#contributing)
13. [License](#license)

---

## **Features**

- **Custom user authentication system** with JWT tokens.
- **OAuth2 authentication** for Google and Apple social logins.
- **User profile management**: view and update profile details.
- **Profile picture upload** with validation.
- **Onboarding modules** for managing work experience and skills.
- **Basic search functionality** to filter users by skills and job experience.
- **Secure password handling** with validation for complexity.
- **Comprehensive API documentation** using Swagger.

---

## **Tech Stack**

- **Backend Framework**: Django, Django REST Framework (DRF)
- **Database**: PostgreSQL
- **Authentication**: JWT for session management, OAuth2 for social logins
- **Image Handling**: Cloudinary (optional, for profile pictures)
- **Documentation**: drf-spectacular (Swagger)

---

## **Prerequisites**

- Python 3.8+
- PostgreSQL 12+
- Node.js (optional, for running frontend or OAuth flows)
- [Cloudinary](https://cloudinary.com/) account (optional, for profile picture uploads)

---

## **Installation**

1. **Clone the repository**:

    ```
    git clone https://github.com/your-username/django-onboarding-backend.git
    cd django-onboarding-backend
    ```

2. **Create a virtual environment**:

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies**:

    ```
    pip install -r requirements.txt
    ```

4. **Set up environment variables** (see [Environment Variables](#environment-variables)).

5. **Configure the database** (see [Database Setup](#database-setup)).

6. **Run migrations**:

    ```
    python manage.py migrate
    ```

---

## **Running the Application**

To start the development server:

```
python manage.py runserver
```

By default, the server will be accessible at `http://127.0.0.1:8000/`.

---

## **Environment Variables**

Create a `.env` file in the project root and add the following environment variables:

```bash
SECRET_KEY=your_secret_key
DEBUG=True  # Set to False in production
ALLOWED_HOSTS=127.0.0.1, localhost

# Database
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# JWT Settings
JWT_SECRET_KEY=your_jwt_secret_key
JWT_ALGORITHM=HS256
JWT_EXPIRATION_TIME=3600

# OAuth2 (for Google, Apple)
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
APPLE_CLIENT_ID=your_apple_client_id
APPLE_CLIENT_SECRET=your_apple_client_secret

# Cloudinary (optional for profile pictures)
CLOUDINARY_NAME=your_cloudinary_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret
```

---

## **Database Setup**

1. **Create a PostgreSQL database**:

   ```
   psql
   CREATE DATABASE your_db_name;
   CREATE USER your_db_user WITH PASSWORD 'your_db_password';
   ALTER ROLE your_db_user SET client_encoding TO 'utf8';
   ALTER ROLE your_db_user SET default_transaction_isolation TO 'read committed';
   ALTER ROLE your_db_user SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;
   \q
   ```

2. **Migrate the database**:

   Run the following command to apply the database migrations:

   ```
   python manage.py migrate
   ```

---

## **API Endpoints**

### **Authentication Endpoints**

| Method | Endpoint               | Description                |
|--------|------------------------|----------------------------|
| POST   | `/api/auth/register/`   | Register a new user        |
| POST   | `/api/auth/login/`      | User login with JWT        |
| POST   | `/api/auth/social-login/google/` | Google OAuth2 login |
| POST   | `/api/auth/social-login/apple/`  | Apple OAuth2 login  |
| POST   | `/api/auth/logout/`     | User logout (invalidate JWT) |

### **User Profile Endpoints**

| Method | Endpoint                | Description              |
|--------|-------------------------|--------------------------|
| GET    | `/api/profile/`          | Get user profile         |
| PUT    | `/api/profile/update/`   | Update user profile      |
| PUT    | `/api/profile/picture/`  | Upload/update profile picture |

### **Onboarding - Work Experience**

| Method | Endpoint                         | Description                          |
|--------|----------------------------------|--------------------------------------|
| GET    | `/api/onboarding/work-experience/` | List all work experience entries     |
| POST   | `/api/onboarding/work-experience/` | Add a new work experience entry      |
| PUT    | `/api/onboarding/work-experience/{id}/` | Update a work experience entry |
| DELETE | `/api/onboarding/work-experience/{id}/` | Delete a work experience entry |

### **Onboarding - Skills and Interests**

| Method | Endpoint                         | Description                          |
|--------|----------------------------------|--------------------------------------|
| GET    | `/api/onboarding/skills/`        | List all skills                     |
| POST   | `/api/onboarding/skills/`        | Add new skills                      |
| PUT    | `/api/onboarding/skills/{id}/`   | Update skills                       |
| DELETE | `/api/onboarding/skills/{id}/`   | Delete skills                       |

### **Search and Filter**

| Method | Endpoint                       | Description                        |
|--------|--------------------------------|------------------------------------|
| GET    | `/api/search/users/`           | Search users by skills or experience |

---

## **Testing**

To run unit tests:

```
python manage.py test
```

---

## **API Documentation**

API documentation is generated using **drf-spectacular** and can be viewed at:

```
http://127.0.0.1:8000/
```

---

## **Database Schema**

The database schema follows best practices for normalization and includes the following tables:

- **User**: Stores basic user information like email, password, etc.
- **Profile**: Extends the user model to include additional fields like profile picture, phone number.
- **WorkExperience**: Stores the user's job experiences with fields like `job title`, `company name`, `start date`, etc.
- **Skill**: Contains a list of user-added or predefined skills.

For an Entity Relationship Diagram (ERD), refer to the `/docs/erd.pdf` file in the project repository.

---

## **Contributing**

We welcome contributions! Please fork this repository and submit a pull request for review.

---
