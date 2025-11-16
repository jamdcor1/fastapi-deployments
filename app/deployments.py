# app/deployments.py

from typing import Dict, List

from . import schemas
from .exceptions import DeploymentNotFoundError

# Simple in-memory store for Phase 0 / Phase 1
_deployments: Dict[int, schemas.Deployment] = {}
_next_id: int = 1


def list_deployments() -> List[schemas.Deployment]:
    return list(_deployments.values())


def create_deployment(payload: schemas.DeploymentCreate) -> schemas.Deployment:
    global _next_id

    deployment = schemas.Deployment(
        id=_next_id,
        name=payload.name,
        environment=payload.environment,
        version=payload.version,
    )
    _deployments[_next_id] = deployment
    _next_id += 1
    return deployment


def get_deployment(deployment_id: int) -> schemas.Deployment:
    deployment = _deployments.get(deployment_id)
    if deployment is None:
        raise DeploymentNotFoundError(deployment_id)
    return deployment


def update_deployment(
    deployment_id: int,
    payload: schemas.DeploymentUpdate,
) -> schemas.Deployment:
    if deployment_id not in _deployments:
        raise DeploymentNotFoundError(deployment_id)

    existing = _deployments[deployment_id]
    updated_data = existing.model_dump()

    # Only overwrite fields that were provided
    for field, value in payload.model_dump(exclude_unset=True).items():
        updated_data[field] = value

    updated = schemas.Deployment(**updated_data)
    _deployments[deployment_id] = updated
    return updated


def delete_deployment(deployment_id: int) -> None:
    if deployment_id not in _deployments:
        raise DeploymentNotFoundError(deployment_id)

    del _deployments[deployment_id]
