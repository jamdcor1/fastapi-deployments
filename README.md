📦 FastAPI Deployments App

A small FastAPI application built as part of a DevOps learning roadmap.
This project grows through multiple phases—starting local-only, then adding best practices, a real database, containers, CI/CD, cloud deployment, and observability.

This README reflects the project as of the end of Phase 1.

🚀 Project Overview

This app provides a simple API to track “deployments” using in-memory storage (for now).
It includes:

/healthz endpoint

Full CRUD for deployments

Pydantic models

Automated FastAPI docs (/docs & /redoc)

Test suite with pytest

Development best practices (linting, logging, config, exception handling)

This forms the foundation for deeper DevOps concepts introduced in later phases.

📁 Project Structure
fastapi-deployments/
│
├── app/
│   ├── main.py               # FastAPI app, routes, logging, exception handlers
│   ├── deployments.py        # In-memory deployment store + CRUD logic
│   ├── schemas.py            # Pydantic models
│   ├── exceptions.py         # Custom exception types
│   └── config.py             # Pydantic Settings loaded from .env
│
├── tests/
│   └── test_deployments.py   # Full test suite for API endpoints
│
├── requirements.txt          # Runtime dependencies
├── requirements-dev.txt      # Ruff, pre-commit, pytest (development only)
├── .pre-commit-config.yaml   # Linting/formatting hooks
├── .gitignore
├── .env.example              # Example environment variables
└── README.md                 # You're reading it!

🧪 Running the Application
1. Create virtual environment & install dependencies
python -m venv .venv
source .venv/bin/activate     # or .venv\Scripts\activate on Windows

pip install -r requirements.txt
pip install -r requirements-dev.txt

2. Create a local .env
cp .env.example .env


Modify values as needed:

APP_NAME=FastAPI Deployments
ENVIRONMENT=local
LOG_LEVEL=INFO

3. Start the API
uvicorn app.main:app --reload


Visit:

Swagger UI → http://localhost:8000/docs

ReDoc → http://localhost:8000/redoc

🧪 Running the Tests
pytest


All tests should pass:

6 passed in X.XXs

🧹 Development Workflow (Phase 1 Practices)
✔ Ruff Linting

Check:

ruff check .


Auto-fix:

ruff check . --fix

✔ Ruff Formatting
ruff format .

✔ Pre-commit Hooks

Install:

pre-commit install


Now every commit automatically:

Formats code

Lints code

Rejects violations

📝 Features Implemented (End of Phase 1)
✔ Phase 0 — Core Local App

FastAPI project structure

CRUD endpoints for deployments

In-memory data store

Pydantic models (v2 style)

Automated tests

Interactive docs

Runs locally with Uvicorn

✔ Phase 1 — Development Best Practices

Ruff linting + formatting

Pre-commit hooks

Logging added to all routes

Centralized exception handling

Configuration via environment variables (Pydantic Settings)

.env.example and .gitignore improvements

Full test suite passing

🔮 Next Phase: Phase 2 — Real Database (SQLite → Postgres)

In Phase 2 we will:

Add SQLModel or SQLAlchemy

Create Deployment database models

Replace in-memory storage

Add Alembic migrations

Use SQLite locally

Add environment-based database URLs

Prepare for Postgres in containers and cloud

📌 About This Project

This repository is part of a multi-phase DevOps learning roadmap designed to simulate:

software development

backend engineering

containerization

CI/CD automation

cloud deployment

observability

At each phase, the project evolves toward production-readiness.