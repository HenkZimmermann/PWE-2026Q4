import pytest
from src.sections.user import user_service
from src.sections.user.user_model import LoginRequest

@pytest.fixture
def login_request():
    return LoginRequest(email="test@example.com", password="test-password")

@pytest.fixture
def stored_user(login_request):
    return {
        "user_id": 7,
        "username": "testuser",
        "email": login_request.email,
        "role_id": 3,
        "password_hash": user_service.hash_password(login_request.password),
    }

def test_login_returns_user_data(monkeypatch, login_request, stored_user):
    users_by_email = {stored_user["email"]: stored_user}
    monkeypatch.setattr(user_service, "get_user_by_email", users_by_email.get)
    assert user_service.check_login_request(login_request) == {
        "user_id": 7,
        "username": "testuser",
        "email": "test@example.com",
        "role": 3,
    }

def test_login_rejects_wrong_password(monkeypatch, login_request, stored_user):
    users_by_email = {stored_user["email"]: stored_user}
    monkeypatch.setattr(user_service, "get_user_by_email", users_by_email.get)
    wrong_password_request = LoginRequest(
        email=login_request.email, password="wrong-password"
    )
    assert user_service.check_login_request(wrong_password_request) is False

def test_login_rejects_unknown_email(monkeypatch, login_request):
    users_by_email = {}
    monkeypatch.setattr(user_service, "get_user_by_email", users_by_email.get)
    assert user_service.check_login_request(login_request) is False

def test_hash_password_accepts_72_utf8_bytes():
    password = "ä" * 36
    password_hash = user_service.hash_password(password)
    assert user_service.verify_password(password, password_hash)

def test_hash_password_rejects_more_than_72_utf8_bytes():
    password = "ä" * 36 + "a"
    with pytest.raises(ValueError):
        user_service.hash_password(password)
