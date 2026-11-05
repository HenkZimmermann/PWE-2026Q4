from fastapi import APIRouter, HTTPException, status
from src.sections.thread.thread_model import *
from src.sections.thread.thread_service import *
router = APIRouter()
@router.get("/threads/votes")
def get_threads_ordered_by_votes_route():
    try:
        threads = get_all_threads_order_by_votes()
        if not threads:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Threads not found")
        return threads
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.post("/threads/create")
def create_thread_route(request: threadCreateModel):
    try:
        thread = create_thread(request)
        return thread
    except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.delete("/threads/{thread_id}")
def delete_thread_route(thread_id: int):
    try:
        result = delete_thread_by_id(thread_id)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Thread not found")
        return {"message": "Thread deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.put("/threads/{thread_id}")
def edit_thread_route(thread_id: int, request: threadCreateModel):
    try:
        result = edit_thread_by_id(thread_id, request)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Thread not found")
        return {"message": "Thread updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.get("/threads/search/{thread_name}")
def get_all_threads_by_name_route(thread_name: str):
    try:
        threads = get_all_threads_by_name(thread_name)
        if not threads:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Thread not found")
        return threads
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.get("/threads/{thread_id}")
def get_thread_by_id_route(thread_id: int):
    try:
        thread = get_thread_by_id(thread_id)
        if not thread:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Thread not found")
        return thread
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.get("/threads/user/{user_id}")
def get_threads_by_user_id_route(user_id: int):
    try:
        threads = get_all_threads_by_user_id(user_id)
        if not threads:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Threads not found")
        return threads
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.get("/threads/group/{group_id}")
def get_threads_by_group_id_route(group_id: int):
    try:
        threads = get_threads_of_group_order_by_date(group_id)
        if not threads:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Threads not found")
        return threads
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))