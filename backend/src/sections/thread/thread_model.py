from pydantic import BaseModel

class ThreadModel(BaseModel):
    message: str
    user_id: int
    votes: int
    group_id: int
    title: str

# Create nimmt kein votes, weil kann ja noch keine haben können bei Erstellung
class CreateThreadModel(ThreadModel):
    votes: int = 0

class EditThreadModel(BaseModel):
    title: str
    message: str
