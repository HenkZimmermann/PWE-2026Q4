from pydantic import BaseModel

class CommentModel(BaseModel):
    thread_id: int
    parent_comment_id: int | None = None
    message: str
    votes: int
    user_id: int

class EditCommentModel(BaseModel):
    message: str
