from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_deployment():
    payload = {"name": "api", "version": "1.0", "environment": "dev"}
    response = client.post("/deployments/", json=payload)
    assert response.status_code == 201
    body = response.json()

    assert body["name"] == "api"
    assert body["version"] == "1.0"
    assert body["environment"] == "dev"
    assert "id" in body


def test_list_deployments():
    response = client.get("/deployments/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_deployment():
    payload = {"name": "web", "version": "2.0", "environment": "prod"}
    created = client.post("/deployments/", json=payload).json()
    dep_id = created["id"]

    response = client.get(f"/deployments/{dep_id}")
    assert response.status_code == 200
    assert response.json()["id"] == dep_id


def test_update_deployment():
    payload = {"name": "app", "version": "3.0", "environment": "dev"}
    created = client.post("/deployments/", json=payload).json()
    dep_id = created["id"]

    update = {"version": "3.1"}
    response = client.put(f"/deployments/{dep_id}", json=update)
    assert response.status_code == 200
    assert response.json()["version"] == "3.1"


def test_delete_deployment():
    payload = {"name": "worker", "version": "1.0", "environment": "qa"}
    created = client.post("/deployments/", json=payload).json()
    dep_id = created["id"]

    response = client.delete(f"/deployments/{dep_id}")
    assert response.status_code == 204

    get_response = client.get(f"/deployments/{dep_id}")
    assert get_response.status_code == 404
