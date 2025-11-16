from fastapi import APIRouter, HTTPException
from app.schemas import Deployment, DeploymentCreate, DeploymentUpdate
from datetime import datetime

router = APIRouter()

# --- In-memory store ---
deployments = {}
next_id = 1


@router.get("/", response_model=list[Deployment])
def list_deployments():
    return list(deployments.values())


@router.post("/", response_model=Deployment, status_code=201)
def create_deployment(payload: DeploymentCreate):
    global next_id

    deployment = Deployment(
        id=next_id,
        name=payload.name,
        version=payload.version,
        environment=payload.environment,
        created_at=datetime.now()
    )
    deployments[next_id] = deployment
    next_id += 1
    return deployment


@router.get("/{deployment_id}", response_model=Deployment)
def get_deployment(deployment_id: int):
    if deployment_id not in deployments:
        raise HTTPException(status_code=404, detail="Deployment not found")
    return deployments[deployment_id]


@router.put("/{deployment_id}", response_model=Deployment)
def update_deployment(deployment_id: int, payload: DeploymentUpdate):
    if deployment_id not in deployments:
        raise HTTPException(status_code=404, detail="Deployment not found")

    stored = deployments[deployment_id]
    updated = stored.copy(update=payload.dict(exclude_unset=True))
    deployments[deployment_id] = updated
    return updated


@router.delete("/{deployment_id}", status_code=204)
def delete_deployment(deployment_id: int):
    if deployment_id not in deployments:
        raise HTTPException(status_code=404, detail="Deployment not found")

    del deployments[deployment_id]
    return None
