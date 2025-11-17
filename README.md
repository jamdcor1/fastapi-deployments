# FastAPI Deployments App

A small FastAPI application built as part of a multi-phase DevOps learning roadmap.  
The project begins as a simple local FastAPI service (Phase 0) and evolves through industry-standard DevOps practices including linting, formatting, configuration, testing, databases, containers, CI/CD, cloud deployment, and observability.

This README reflects the project **as of the completion of Phase 1**.

---

## Overview

This application provides:

- `/healthz` – health check endpoint  
- `/deployments` – CRUD API for deployments  
- Automatic API docs via Swagger (`/docs`) and ReDoc (`/redoc`)  
- A pytest test suite  
- In-memory storage (database integration begins in Phase 2)

Phase 1 also introduced:

- Ruff linting and formatting  
- Pre-commit hooks  
- Structured logging  
- Centralized exception handling  
- Environment-based configuration using Pydantic Settings  

---

## Project Structure

fastapi-deployments/
│
├── app/
│ ├── main.py # FastAPI app, routes, logging, exception handlers
│ ├── deployments.py # In-memory deployment store + CRUD logic
│ ├── schemas.py # Pydantic models
│ ├── exceptions.py # Custom exception classes
│ └── config.py # Environment-based configuration (Pydantic Settings)
│
├── tests/
│ └── test_deployments.py # Test suite for API endpoints
│
├── requirements.txt # Runtime dependencies
├── requirements-dev.txt # Development tools (ruff, pre-commit, pytest)
├── .pre-commit-config.yaml # Pre-commit hook definitions
├── .gitignore
├── .env.example # Sample environment variable file
└── README.md


---

## Setup Instructions

### 1. Create a virtual environment

python -m venv .venv



Activate it:

**Windows:**
.venv\Scripts\activate



**macOS/Linux:**
source .venv/bin/activate


---

### 2. Install dependencies

pip install -r requirements.txt
pip install -r requirements-dev.txt


---

### 3. Create your `.env` file

Copy the example:

cp .env.example .env



Edit values as needed:

APP_NAME=FastAPI Deployments

ENVIRONMENT=local

LOG_LEVEL=INFO


---

### 4. Start the API

uvicorn app.main:app --reload


Visit:

- Swagger UI → http://localhost:8000/docs  
- ReDoc → http://localhost:8000/redoc  

---

## Running Tests

Tests use pytest and FastAPI’s TestClient.

pytest



Expected:

6 passed in X.XXs


---

## Development Workflow (Phase 1 Practices)

### Ruff Linting

ruff check .



Auto-fix:

ruff check . --fix



### Ruff Formatting

ruff format .



### Pre-commit Hooks

Install and enable:

pre-commit install


From now on, every commit will:

- Format code  
- Lint code  
- Fail if issues are detected  

---

## Phase 0 Features (Completed)

- FastAPI app scaffold  
- `/healthz` endpoint  
- CRUD endpoints for deployments  
- In-memory storage  
- Pydantic schemas  
- Interactive API docs  
- Full pytest test suite  
- Local development with Uvicorn  

---

## Phase 1 Features (Completed)

- Linting using Ruff  
- Formatting using Ruff  
- Pre-commit automation  
- Logging added to all endpoints  
- Centralized exception handling  
- Pydantic Settings for environment variables  
- `.env.example` configuration baseline  
- Improved `.gitignore`  
- 100% passing test suite  

---

## Next Phase: Phase 2 – Real Database Integration

Phase 2 will introduce:

- SQLModel or SQLAlchemy ORM  
- SQLite for local dev  
- Postgres for production/cloud  
- Alembic migrations  
- Database URL config via environment variables  
- CRUD rewritten to use the database instead of in-memory storage  

---

## Purpose of This Repository

This project is part of a long-term DevOps learning roadmap, designed to teach:

- Python application development  
- API design and structure  
- Code quality and linting  
- Testing best practices  
- Configuration management  
- Containerization (Docker)  
- CI/CD automation (GitHub Actions)  
- Cloud deployment  
- Observability and monitoring  

Each phase brings this application closer to real-world production standards.

---
