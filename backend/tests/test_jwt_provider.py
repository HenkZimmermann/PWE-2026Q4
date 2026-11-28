import pytest
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from src.security import jwtProvider

def test_valid_token_returns_user_data():
    user = {
        "user_id": 7,
        "username": "testuser",
        "email": "test@example.com",
        "role": 3,
    }
    token = jwtProvider.create_access_token(user)
    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials=token)

    assert jwtProvider.get_current_user(credentials) == user

def test_token_without_user_id_is_rejected():
    token = jwtProvider.create_access_token({"username": "testuser"})
    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials=token)

    with pytest.raises(HTTPException) as error:
        jwtProvider.get_current_user(credentials)

    assert error.value.status_code == 401

def test_expired_token_is_rejected(monkeypatch):
    monkeypatch.setattr(jwtProvider, "ACCESS_TOKEN_EXPIRE_MINUTES", -1)
    token = jwtProvider.create_access_token({"user_id": 7})
    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials=token)

    with pytest.raises(HTTPException) as error:
        jwtProvider.get_current_user(credentials)

    assert error.value.status_code == 401
