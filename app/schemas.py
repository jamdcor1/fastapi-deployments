from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DeploymentBase(BaseModel):
    name: str
    version: str
    environment: str


class DeploymentCreate(DeploymentBase):
    pass


class DeploymentUpdate(BaseModel):
    name: Optional[str] = None
    version: Optional[str] = None
    environment: Optional[str] = None


class Deployment(DeploymentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
