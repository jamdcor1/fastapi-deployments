# FastAPI Deployments App (Phase 0)

A minimal FastAPI application for learning DevOps fundamentals.

## Features
- FastAPI local app
- In-memory CRUD for deployments
- `/healthz` endpoint
- Pydantic schemas
- Pytest automated tests
- Interactive docs at `/docs`

## Running the App
```bash
uvicorn app.main:app --reload
