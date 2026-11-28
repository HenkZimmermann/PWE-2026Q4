from pydantic import BaseModel

class ThreadVoteRequest(BaseModel):
    direction: int
