# app/exceptions.py


class DeploymentNotFoundError(Exception):
    """Raised when a deployment with the given ID does not exist."""

    def __init__(self, deployment_id: int) -> None:
        self.deployment_id = deployment_id
        super().__init__(f"Deployment {deployment_id} not found")
