from fastapi import APIRouter, HTTPException, status
from src.sections.member_of.member_of_service import *

router = APIRouter()

@router.post("/member_of/create")
def create_group_membership_route(user_id: int, group_id: int):
    try:
        member = create_group_membership(user_id, group_id)
        if not member:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Group membership could not be created")
        return member
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.delete("/member_of/delete")
def delete_group_membership_route(user_id: int, group_id: int):
    try:
        result = delete_group_membership(user_id, group_id)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group membership not found")
        return {"message": "Group membership deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/member_of/members/{group_id}")
def get_all_members_of_group_id_route(group_id: int):
    try:
        members = get_all_members_of_group_id(group_id)
        if not members:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Members not found")
        return members
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/member_of/memberships/{user_id}")
def get_memberships_from_user_id_route(user_id: int):   
    try:
        memberships = get_memberships_from_user_id(user_id)
        if not memberships:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Memberships not found")
        return memberships
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))