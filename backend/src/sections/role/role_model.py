from pydantic import BaseModel

class RoleModel(BaseModel):
    name: str
    permissions: str
