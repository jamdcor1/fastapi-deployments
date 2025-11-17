# app/main.py

import logging
from typing import List

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from . import deployments, schemas
from .config import settings
from .exceptions import DeploymentNotFoundError

# -----------------------------
# Logging configuration
# -----------------------------
logging.basicConfig(
    level=settings.log_level.upper(),
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger("deployments_app")

logger.info(
    "Starting app '%s' in environment '%s' with log level '%s'",
    settings.app_name,
    settings.environment,
    settings.log_level.upper(),
)

# -----------------------------
# FastAPI app
# -----------------------------
app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
)


# -----------------------------
# Exception handlers
# -----------------------------
@app.exception_handler(DeploymentNotFoundError)
async def deployment_not_found_handler(
    request: Request,
    exc: DeploymentNotFoundError,
) -> JSONResponse:
    logger.warning(
        "Deployment not found: id=%s path=%s",
        exc.deployment_id,
        request.url.path,
    )
    # Keep the message simple to match tests
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Deployment not found"},
    )


# -----------------------------
# Routes
# -----------------------------
@app.get("/healthz")
def healthz() -> dict:
    logger.debug("Health check requested")
    # Keep this EXACT for tests
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
        "Creating deployment: name=%s, environment=%s, version=%s",
        payload.name,
        payload.environment,
        payload.version,
    )
    deployment = deployments.create_deployment(payload)
    logger.info("Created deployment id=%s", deployment.id)
    return deployment


@app.get("/deployments/{deployment_id}", response_model=schemas.Deployment)
def get_deployment(deployment_id: int) -> schemas.Deployment:
    logger.info("Fetching deployment id=%s", deployment_id)
    deployment = deployments.get_deployment(deployment_id)
    if deployment is None:
        raise DeploymentNotFoundError(deployment_id)
    logger.info("Fetched deployment id=%s", deployment_id)
    return deployment


@app.put("/deployments/{deployment_id}", response_model=schemas.Deployment)
def update_deployment(
    deployment_id: int,
    payload: schemas.DeploymentUpdate,
) -> schemas.Deployment:
    logger.info("Updating deployment id=%s", deployment_id)
    updated = deployments.update_deployment(deployment_id, payload)
    if updated is None:
        raise DeploymentNotFoundError(deployment_id)
    logger.info("Updated deployment id=%s", deployment_id)
    return updated


@app.delete("/deployments/{deployment_id}", status_code=204)
def delete_deployment(deployment_id: int) -> None:
    logger.info("Deleting deployment id=%s", deployment_id)
    deleted = deployments.delete_deployment(deployment_id)
    if not deleted:
        raise DeploymentNotFoundError(deployment_id)
    logger.info("Deleted deployment id=%s", deployment_id)
    # 204 with JSON body is a very test-friendly shape
    return None
