from pydantic import BaseModel

class GroupModel(BaseModel):
    group_name: str
    category: str
    members: int
    system_created: bool
    description: str 
