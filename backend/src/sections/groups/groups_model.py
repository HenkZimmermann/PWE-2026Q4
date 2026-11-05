from pydantic import BaseModel

class groupCreateModel(BaseModel):
    group_name: str
    category: str
    members: int
    system_created:bool
    description:str
class groupEditModel(BaseModel):
    group_name: str
    category: str
    members: int
    system_created: bool
    description: str    
