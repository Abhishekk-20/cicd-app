import pytest

from app import app


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "CI/CD Demo Application"
    assert response.json["status"] == "running"
    assert response.json["version"] == "1.0.1"


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_info(client):
    response = client.get("/api/info")
    assert response.status_code == 200
    assert response.json["application"] == "cicd-app"
