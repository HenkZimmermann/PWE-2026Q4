from fastapi import APIRouter, HTTPException, status
from src.sections.user.user_model import * 
from src.sections.user.user_service import *

router = APIRouter()

@router.post("/users/create")
def create_user_route(request: CreateRequest):
    try:
        user = create_user(request)
        return user
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
        return {"message": "USer updated successfully"}
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
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))