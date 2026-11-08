from fastapi import APIRouter, HTTPException, status
from src.sections.comment.comment_model import *
from src.sections.comment.comment_service import *

router = APIRouter()

@router.post("/comments/create")
def create_comment_route(request: commentCreateModel):
    try:
        comment = create_comment(request)
        return comment
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/comments/{comment_id}")
def delete_comment_route(comment_id: int):
    try:
        result = delete_comment_by_id(comment_id)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
        return {"message": "Comment deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.put("/comments/{comment_id}")
def edit_comment_route(comment_id: int, request: commentCreateModel):
    try:
        result = edit_comment_by_id(comment_id, request)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
        return {"message": "Comment updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/comments/thread/{parent_comment_id}")
def get_comments_by_parent_comment_id_route(parent_comment_id: int):
    try:
        comments = get_all_comments_by_parent_comment_id(parent_comment_id)
        return comments
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/comments/thread/{thread_id}")
def get_comments_by_thread_id_route(thread_id: int):
    try:
        comments = get_all_comments_by_thread_id(thread_id)
        return comments
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/comments/{comment_id}")
def get_comment_by_id_route(comment_id: int):
    try:
        comment = get_comment_by_id(comment_id)
        if not comment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
        return comment
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))