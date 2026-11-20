from fastapi import APIRouter, HTTPException, Query, status
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
def edit_thread_route(thread_id: int, request: ThreadModel):
    try:
        result = edit_thread_by_id(thread_id, request)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Thread not found")
        return {"message": "Thread updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
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
