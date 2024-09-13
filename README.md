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

---

## **Features**

- **Custom user authentication system** with JWT tokens.
- **OAuth2 authentication** for Google social logins.
- **User profile management**: view and update profile details.
- **Profile picture upload** with validation.
- **Onboarding modules** for managing work experience skills, interests.
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
- Django Rest Framework
- PostgreSQL 12+
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

# Database
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# OAuth2 (for Google)
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret

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

3. **Populate the database**:

   Run the following command to apply skills and interest to the database population:

   ```
   python manage.py populate_data.py
   ```

---

## **API Endpoints**


---


# API Endpoints Documentation

## Authentication Endpoints

| Method | Endpoint                          | Description                       |
|--------|-----------------------------------|-----------------------------------|
| POST   | `/api/v1/auth/register/`           | Register a new user               |
| POST   | `/api/v1/auth/login/`              | User login with JWT               |
| POST   | `/api/v1/auth/social-login/google/` | Google OAuth2 login               |


## User Profile Endpoints

| Method | Endpoint                  | Description              |
|--------|---------------------------|--------------------------|
| GET    | `/api/v1/profile/`        | Get user profile         |
| PUT    | `/api/v1/profile/update/` | Update user profile      |

## Onboarding - Work Experience

| Method | Endpoint                          | Description                          |
|--------|-----------------------------------|--------------------------------------|
| GET    | `/api/v1/work/experiences/`       | List all work experience entries     |
|  GET   |  `/api/v1/work/experiences/<uuid:pk>/` | List work experience details        |
| POST   | `/api/v1/work/experiences/create/` | Add a new work experience entry      |
| PUT    | `/api/v1/work/experiences/<uuid:pk>/edit/` | Update a work experience entry       |
| DELETE | `/api/v1/work/experiences/<uuid:pk>/delete/` | Delete a work experience entry       |

## Onboarding - Skills and Interests

| Method | Endpoint                            | Description                          |
|--------|-------------------------------------|--------------------------------------|
| GET    | `/api/v1/skills/`                   | List all skills                      |
| POST   | `/api/v1/user-skills/add/`          | Add new skill to user profile        |
| GET    | `/api/v1/user-skills/add/`          | Add new user skill (to be clarified) |
| GET    | `/api/v1/user-skills/user-skills/`  | List user skills                     |
| DELETE | `/api/v1/user-skills/<uuid:pk>/delete/` | Delete user skill                    |
| GET    | `/api/v1/users/search/`             | Search for users                     |
| GET    | `/api/v1/user-interests/`           | List user interests                  |
| POST   | `/api/v1/user-interests/add/`       | Add new user interest                |
| DELETE | `/api/v1/user-interests/<uuid:pk>/delete/` | Delete user interest                 |
| GET    | `/api/v1/interests/`                | List all predefined interests        |



## Search and Filter

| Method | Endpoint                | Description                        |
|--------|-------------------------|------------------------------------|
| GET    | `/api/v1/users/search/` | Search users by skills or experience |

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



#### 1. **User Table**

```sql
CREATE TABLE User (
    id CHAR(36) PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(50) NOT NULL,
    phone VARCHAR(20),
    profile_picture VARCHAR(255),
);
```

**Fields:**
- `id`: UUID primary key (CHAR(36)).
- `email`: Unique email address.
- `name`: User’s name.
- `phone`: Optional phone number.
- `profile_picture`: URL or path to the profile picture.

---

#### 2. **WorkExperience Table**

```sql
CREATE TABLE WorkExperience (
    id CHAR(36) PRIMARY KEY,
    user_id CHAR(36),
    job_title VARCHAR(100) NOT NULL,
    company_name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    job_type VARCHAR(50) CHECK (job_type IN ('Full-time', 'Part-time', 'Contract')) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    description TEXT,
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
);
```

**Fields:**
- `id`: UUID primary key (CHAR(36)).
- `user_id`: UUID foreign key (CHAR(36)).
- `job_title`: Job title.
- `company_name`: Company name.
- `location`: Job location.
- `job_type`: Employment type.
- `start_date`: Start date.
- `end_date`: End date (optional).
- `description`: Job description.

---

#### 3. **Skill Table**

```sql
CREATE TABLE Skill (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
);
```

**Fields:**
- `id`: UUID primary key (CHAR(36)).
- `name`: Skill name.

---

#### 4. **Interest Table**

```sql
CREATE TABLE Interest (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
);
```

**Fields:**
- `id`: UUID primary key (CHAR(36)).
- `name`: Interest name.

---

#### 5. **UserSkill Table**

```sql
CREATE TABLE UserSkill (
    id CHAR(36) PRIMARY KEY,
    user_id CHAR(36),
    skill_id CHAR(36),
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
    FOREIGN KEY (skill_id) REFERENCES Skill(id) ON DELETE CASCADE,
);
```

**Fields:**
- `id`: UUID primary key (CHAR(36)).
- `user_id`: UUID foreign key (CHAR(36)).
- `skill_id`: UUID foreign key (CHAR(36)).

---

#### 6. **UserInterest Table**

```sql
CREATE TABLE UserInterest (
    id CHAR(36) PRIMARY KEY,
    user_id CHAR(36),
    interest_id CHAR(36),
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
    FOREIGN KEY (interest_id) REFERENCES Interest(id) ON DELETE CASCADE,
);
```

**Fields:**
- `id`: UUID primary key (CHAR(36)).
- `user_id`: UUID foreign key (CHAR(36)).
- `interest_id`: UUID foreign key (CHAR(36)).

---

### Relationships Summary

- **User** has a one-to-many relationship with **WorkExperience**, **UserSkill**, and **UserInterest**.
- **WorkExperience** is linked to **User** via `user_id`.
- **UserSkill** links **User** and **Skill**.
- **UserInterest** links **User** and **Interest**.
- **Skill** and **Interest** have a one-to-many relationship with **UserSkill** and **UserInterest**, respectively.

This schema ensures that UUIDs are used consistently for primary keys and foreign keys, and it maintains the integrity of the relationships between tables.

For an Entity Relationship Diagram (ERD), refer to the [database diagram](https://drawsql.app/teams/lonestarr/diagrams/gdsc-task).

---

## **Contributing**

We welcome contributions! Please fork this repository and submit a pull request for review.

---
