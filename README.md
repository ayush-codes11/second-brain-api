# Second Brain API

A scalable backend API for a personal knowledge management system built using FastAPI, PostgreSQL, Docker, JWT authentication, and Alembic migrations.

The project is designed as the foundation for an AI-powered “second brain” application where users can securely manage and organize their notes and knowledge.

---

# Features

* User authentication with JWT
* Protected API routes
* Multi-user authorization
* CRUD operations for notes
* PostgreSQL database integration
* Dockerized database setup
* Alembic database migrations
* Environment variable configuration
* FastAPI automatic Swagger documentation

---

# Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Docker
* Alembic
* JWT Authentication
* Pydantic
* Python

---

# Project Structure

```bash
second-brain-api/
│
├── alembic/
├── app/
│   ├── auth/
│   ├── db/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   └── main.py
│
├── .env
├── .gitignore
├── alembic.ini
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/ayush-codes11/second-brain-api.git
```

## 2. Navigate Into Project Folder

```bash
cd second-brain-api
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<database_name>

SECRET_KEY=your_secret_key
```

---

# Run PostgreSQL Using Docker

## Pull PostgreSQL Image

```bash
docker pull postgres
```

## Create PostgreSQL Container

```bash
docker run --name second-brain-db \
-e POSTGRES_USER=postgres \
-e POSTGRES_PASSWORD=password \
-e POSTGRES_DB=second_brain_db \
-p 5432:5432 \
-d postgres
```

## Start Existing Container

```bash
docker start second-brain-db
```

---

# Database Migrations

## Generate Migration

```bash
alembic revision --autogenerate -m "migration message"
```

## Apply Migration

```bash
alembic upgrade head
```

---

# Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

# API Documentation

Swagger documentation is available at:

```bash
http://127.0.0.1:8000/docs
```

---

# Authentication

The API uses JWT-based authentication.

After login:

* copy the generated access token
* click "Authorize" in Swagger UI
* enter:

```bash
Bearer YOUR_ACCESS_TOKEN
```

---

# Current Functionalities

* User Signup
* User Login
* JWT Authentication
* Protected Routes
* Create Notes
* Get User-Specific Notes
* Database Migrations
* Environment Variable Configuration

---

# Future Roadmap

* AI-powered semantic search
* Vector database integration
* OpenAI integration
* Document upload support
* Redis caching
* Background task processing
* Deployment pipeline
* Frontend integration

---

# Learning Goals

This project was built to strengthen backend engineering concepts including:

* REST API development
* Authentication & Authorization
* Database design
* ORM relationships
* Docker fundamentals
* Database migrations
* Environment configuration
* Backend project structuring

---

# License

This project is for learning and portfolio purposes.
