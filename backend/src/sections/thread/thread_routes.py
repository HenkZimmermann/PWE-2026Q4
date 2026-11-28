from fastapi import APIRouter, Depends, HTTPException, Query, status
from psycopg2 import Error
from src.security.jwtProvider import get_current_user
from src.sections.thread.thread_model import *
from src.sections.thread.thread_service import *

router = APIRouter()

@router.get("/threads/feed")
def get_thread_feed_route(limit: int, group_id: int | None = None):
    # Wir laden hier einen mehr, damit wir unten den check machen obs noch mehr gibt
    # Wir geben aber nur limit Threads zurück
    threads = get_thread_feed(limit + 1, group_id)
    if threads is False:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Feed could not be loaded")

    return {"threads": threads[:limit], "hasMore": len(threads) > limit}

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
def create_thread_route(request: CreateThreadModel):
    thread = create_thread(request)
    if not thread:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Thread could not be created")
    return thread
    
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
def edit_thread_route(thread_id: int, request: EditThreadModel, current_user: dict = Depends(get_current_user)):
    request.title = request.title.strip()
    if not request.title or len(request.title) > 255 or not request.message.strip():
        raise HTTPException(status_code=422, detail="A title of up to 255 characters and a message are required")

    try:
        updated = edit_thread_by_id(thread_id, request, current_user["user_id"], current_user["role"] == 1)
    except Error:
        raise HTTPException(status_code=500, detail="Thread could not be updated")

    if updated is None:
        raise HTTPException(status_code=404, detail="Thread not found")
    if not updated:
        raise HTTPException(status_code=403, detail="Only the author or an admin can edit this thread")
    return {"message": "Thread updated successfully"}
    
@router.get("/threads/search")
def search_threads_route(search_term: str, limit: int, group_id: int | None = None):
    term = search_term.strip()
    if not term:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Search term is required")

    results = search_threads(term, limit, group_id)
    if results is False:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Search could not be completed")

    return {
        "threads": results["threads"],
        "totalCount": results["totalCount"],
        "hasMore": results["totalCount"] > limit,
    }
    
@router.get("/threads/{thread_id}")
def get_thread_by_id_route(thread_id: int):
    thread = get_thread_by_id(thread_id)
    if thread is False:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Thread could not be loaded")
    
    if thread is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Thread not found")
    
    return thread
    
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
