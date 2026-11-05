from fastapi import APIRouter, HTTPException, status
from src.sections.groups.groups_model import *
from src.sections.groups.groups_service import *
router = APIRouter()

@router.post("/groups/create")
def create_group_route(request: groupCreateModel):
    try:
        group = create_group(request)
        return group
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.delete("/groups/{group_id}")
def delete_group_route(group_id: int):
    try:
        result = delete_group_by_id(group_id)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
        return {"message": "Group deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.put("/groups/{group_id}")
def edit_group_route(group_id: int, request: groupEditModel):
    try:
        result = edit_group_by_id(group_id, request)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
        return {"message": "Group updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.get("/groups/category/{category}")
def get_groups_by_category_route(category: str):
    try:
        groups = get_all_groups_by_Category(category)
        return groups
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.get("/groups/members")
def get_groups_by_members_route():
    try:
        groups = get_all_groups_order_by_members()
        return groups
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.get("/groups/all")
def get_all_groups_route():
    try:
        groups = get_all_groups()
        return groups
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.get("/groups/id/{group_id}")
def get_group_by_id_route(group_id: int):
    try:
        group = get_group_by_id(group_id)
        if not group:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
        return group
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.get("/groups/name/{group_name}")
def get_group_by_name_route(group_name: str):
    try:
        group = get_group_by_name(group_name)
        if not group:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
        return group
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    