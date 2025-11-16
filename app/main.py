# app/main.py
import logging
from typing import List

from fastapi import FastAPI, HTTPException

from . import deployments, schemas

# -----------------------------
# Logging configuration
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger("deployments_app")

# -----------------------------
# FastAPI app
# -----------------------------
app = FastAPI(
    title="FastAPI Deployments App",
    version="0.1.0",
)


@app.get("/healthz")
def healthz() -> dict:
    logger.debug("Health check requested")
    return {"status": "ok"}


@app.get("/deployments", response_model=List[schemas.Deployment])
def list_deployments() -> List[schemas.Deployment]:
    logger.info("Listing deployments")
    items = deployments.list_deployments()
    logger.info("Found %s deployments", len(items))
    return items


@app.post("/deployments", response_model=schemas.Deployment, status_code=201)
def create_deployment(payload: schemas.DeploymentCreate) -> schemas.Deployment:
    logger.info(
        "Creating deployment: name=%s, environment=%s",
        payload.name,
        payload.environment,
    )
    deployment = deployments.create_deployment(payload)
    logger.info("Created deployment id=%s", deployment.id)
    return deployment


@app.get("/deployments/{deployment_id}", response_model=schemas.Deployment)
def get_deployment(deployment_id: int) -> schemas.Deployment:
    logger.info("Fetching deployment id=%s", deployment_id)
    deployment = deployments.get_deployment(deployment_id)
    if deployment is None:
        logger.warning("Deployment not found id=%s", deployment_id)
        raise HTTPException(status_code=404, detail="Deployment not found")
    return deployment


@app.put("/deployments/{deployment_id}", response_model=schemas.Deployment)
def update_deployment(
    deployment_id: int,
    payload: schemas.DeploymentUpdate,
) -> schemas.Deployment:
    logger.info("Updating deployment id=%s", deployment_id)
    updated = deployments.update_deployment(deployment_id, payload)
    if updated is None:
        logger.warning("Attempted update on missing deployment id=%s", deployment_id)
        raise HTTPException(status_code=404, detail="Deployment not found")
    logger.info("Updated deployment id=%s", deployment_id)
    return updated


@app.delete("/deployments/{deployment_id}", status_code=204)
def delete_deployment(deployment_id: int) -> None:
    logger.info("Deleting deployment id=%s", deployment_id)
    deleted = deployments.delete_deployment(deployment_id)
    if not deleted:
        logger.warning("Attempted delete on missing deployment id=%s", deployment_id)
        raise HTTPException(status_code=404, detail="Deployment not found")
    logger.info("Deleted deployment id=%s", deployment_id)
