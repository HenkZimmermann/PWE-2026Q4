from src.sections.user import user_routes
from src.security import jwtProvider

def test_login_token_can_load_current_user(client, monkeypatch):
    user = {
        "user_id": 7,
        "username": "testuser",
        "email": "test@example.com",
        "role": 3,
    }

    def check_login(request):
        assert request.email == user["email"]
        assert request.password == "test-password"
        return user

    monkeypatch.setattr(user_routes, "check_login_request", check_login)

    login = client.post(
        "/users/login", json={"email": user["email"], "password": "test-password"}
    )
    assert login.status_code == 200
    assert login.json()["token_type"] == "bearer"

    token = login.json()["accessToken"]
    profile = client.get("/users/me", headers={"Authorization": f"Bearer {token}"})

    assert profile.status_code == 200
    assert profile.json() == {"success": True, **user}


def test_login_rejects_incorrect_credentials(client, monkeypatch):
    monkeypatch.setattr(user_routes, "check_login_request", lambda request: False)

    response = client.post(
        "/users/login", json={"email": "test@example.com", "password": "wrong-password"}
    )

    assert response.status_code == 401
    assert "accessToken" not in response.json()


def test_current_user_rejects_expired_token(client, monkeypatch):
    monkeypatch.setattr(jwtProvider, "ACCESS_TOKEN_EXPIRE_MINUTES", -1)
    token = jwtProvider.create_access_token({"user_id": 7})

    response = client.get("/users/me", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 401
