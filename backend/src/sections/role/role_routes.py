from fastapi import APIRouter, HTTPException, status
from src.sections.role.role_model import *
from src.sections.role.role_service import *
router = APIRouter()

@router.post("/roles/create")
def create_role_route(request: roleCreateModel):
    try:
        role = create_role(request)
        return role
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.put("/roles/{role_id}")
def edit_role_route(role_id: int, request: roleCreateModel):
    try:
        result = edit_role_by_id(role_id, request)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
        return {"message": "Role updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.get("/roles/all")
def get_all_roles_route():
    try:
        roles = get_all_roles()
        return roles
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.get("/roles/{role_id}")
def get_role_by_id_route(role_id: int):
    try:
        role = get_role_by_id(role_id)
        if not role:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
        return role
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))