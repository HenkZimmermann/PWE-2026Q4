from fastapi import APIRouter, HTTPException, status
from src.sections.vote.vote_service import *

router = APIRouter()

@router.post("/vote/create")
def create_follower_route(user_id: int, thread_id: int):
    try:
        vote = create_vote(user_id, thread_id)
        if not vote:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Vote could not be created")
        return vote
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.delete("/votes/delete")
def delete_vote_route(user_id: int, thread_id: int):
    try:
        result = delete_vote(user_id, thread_id)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote not found")
        return {"message": "Vote deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/votes/thread/{thread_id}")
def get_thread_votes_route(thread_id: int):
    try:
        votes = get_thread_votes(thread_id)
        if not votes:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Votes not found")
        return votes
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/votes/user/{user_id}")
def get_votes_by_user_id_route(user_id: int):   
    try:
        votes = get_votes_by_user_id(user_id)
        if not votes:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Votes not found")
        return votes
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))