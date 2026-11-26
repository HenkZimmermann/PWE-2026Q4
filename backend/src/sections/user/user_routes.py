from fastapi import APIRouter, HTTPException, status, Depends
from src.sections.user.user_model import * 
from src.sections.user.user_service import *
from src.security.jwtProvider import create_access_token, get_current_user


router = APIRouter()
@router.get("/users/me")
def get_me(current_user: dict = Depends(get_current_user)):
    return {
        "success": True,
        "user_id": current_user["user_id"],
        "email": current_user["email"],
        "role": current_user["role"],
    }

@router.post("/users/login")
def login(data: LoginRequest):
    user = check_login_request(data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-Mail oder Passwort falsch!",
        )
    access_token = create_access_token(
        data={
            "user_id": user["user_id"],
            "email": user["email"],
            "role": user["role"],
        }
    )
    return {
        "success": True,
        "accessToken": access_token,
        "token_type": "bearer",
    }

@router.post("/users/create")
def create_user_route(request: CreateRequest):
    try:
        # User noch nicht registriert
        if get_user_by_email(request.email) is None:
            create_user(request)
            return True
        else:
            return False
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/user/all")
def get_all_users_route():
    try:
        users = get_all_users()
        if not users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Users not found")
        return users
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.delete("/users/{user_id}")
def delete_user_route(user_id: int):
    try:
        result = delete_user(user_id)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return {"message": "User deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.put("/users/{user_id}")
def edit_user_route(user_id: int, request: EditRequest):
    try:
        result= edit_user_by_id(user_id, request)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return {"message": "User updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))  
       
@router.get("/users/id/{user_id}")
def get_user_by_id_route(user_id: int):
    try:
        user = get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/users/email/{email}")
def get_user_by_id_route(email: EmailStr):
    try:
        user = get_user_by_email(email)
        if not user:
            return False
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))