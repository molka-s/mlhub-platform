from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_register_user():
    response = client.post("/api/v1/auth/register", json={
        "email": "ci@mlhub.com",
        "username": "ciuser",
        "password": "password123"
    })
    assert response.status_code in [201, 400]  # 400 si déjà existant

def test_login_user():
    # Register d'abord
    client.post("/api/v1/auth/register", json={
        "email": "login@mlhub.com",
        "username": "loginuser",
        "password": "password123"
    })
    # Puis login
    response = client.post("/api/v1/auth/login", json={
        "email": "login@mlhub.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()