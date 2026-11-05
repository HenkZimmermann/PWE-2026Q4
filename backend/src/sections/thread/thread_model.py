from pydantic import BaseModel
class threadCreateModel(BaseModel):
    message: str
    user_id: int
    votes: int
    group_id: int
    title: str
