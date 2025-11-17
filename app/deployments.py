# app/deployments.py
from typing import Dict, List, Optional

from datetime import datetime

from . import schemas

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
        created_at=datetime.utcnow(),
    )
    _deployments[_next_id] = deployment
    _next_id += 1
    return deployment


def get_deployment(deployment_id: int) -> Optional[schemas.Deployment]:
    return _deployments.get(deployment_id)


def update_deployment(
    deployment_id: int,
    payload: schemas.DeploymentUpdate,
) -> Optional[schemas.Deployment]:
    existing = _deployments.get(deployment_id)
    if existing is None:
        return None

    # Pydantic v2 style
    updated_data = existing.model_dump()
    update_data = payload.model_dump(exclude_unset=True)
    updated_data.update(update_data)

    updated = schemas.Deployment(**updated_data)
    _deployments[deployment_id] = updated
    return updated


def delete_deployment(deployment_id: int) -> bool:
    if deployment_id in _deployments:
        del _deployments[deployment_id]
        return True
    return False
