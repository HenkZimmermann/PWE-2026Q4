from pydantic import BaseModel
class roleCreateModel(BaseModel):
    name: str
    permissions: str
