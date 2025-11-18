# app/deployments.py
from typing import Sequence

from fastapi import HTTPException, status
from sqlalchemy import select, delete as sqla_delete
from sqlalchemy.orm import Session

from app import schemas
from app.models import Deployment


def list_deployments(db: Session) -> Sequence[Deployment]:
    stmt = select(Deployment)
    return db.scalars(stmt).all()


def get_deployment(db: Session, deployment_id: int) -> Deployment:
    deployment = db.get(Deployment, deployment_id)
    if deployment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Deployment with id {deployment_id} not found",
        )
    return deployment


def create_deployment(db: Session, payload: schemas.DeploymentCreate) -> Deployment:
    deployment = Deployment(
        name=payload.name,
        version=payload.version,
        environment=payload.environment,
    )
    db.add(deployment)
    db.commit()
    db.refresh(deployment)
    return deployment


def update_deployment(
    db: Session,
    deployment_id: int,
    payload: schemas.DeploymentUpdate,
) -> Deployment:
    deployment = get_deployment(db, deployment_id)

    if payload.name is not None:
        deployment.name = payload.name
    if payload.version is not None:
        deployment.version = payload.version
    if payload.environment is not None:
        deployment.environment = payload.environment

    db.commit()
    db.refresh(deployment)
    return deployment


def delete_deployment(db: Session, deployment_id: int) -> bool:
    stmt = sqla_delete(Deployment).where(Deployment.id == deployment_id)
    result = db.execute(stmt)
    db.execute(stmt)
    db.commit()
    return result.rowcount > 0
