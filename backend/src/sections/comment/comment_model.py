from pydantic import BaseModel

class commentCreateModel(BaseModel):
    thread_id: int
    parent_comment_id: int
    message: str
    votes: int
    user_id: int
