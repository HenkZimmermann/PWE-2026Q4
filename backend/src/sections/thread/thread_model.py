from pydantic import BaseModel

class ThreadModel(BaseModel):
    message: str
    user_id: int
    votes: int
    group_id: int
    title: str

# Thread create nimmt kein votes, weil kann ja noch keine haben
class CreateThreadModel(ThreadModel):
    votes: int = 0
