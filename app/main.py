from fastapi import FastAPI
from app.deployments import router as deployments_router

app = FastAPI(title="Deployments API", version="0.1")

@app.get("/healthz")
def health():
    return {"status": "ok"}

app.include_router(deployments_router, prefix="/deployments", tags=["deployments"])
