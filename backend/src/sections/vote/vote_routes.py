from fastapi import APIRouter, Depends, HTTPException, status
from psycopg2 import Error
from src.security.jwtProvider import get_current_user
from src.sections.vote.vote_model import ThreadVoteRequest
from src.sections.vote.vote_service import *

router = APIRouter()

@router.get("/threads/{thread_id}/vote")
def get_thread_vote_route(thread_id: int, current_user: dict = Depends(get_current_user)):
    try:
        vote = get_thread_vote_summary(current_user["user_id"], thread_id)
    except Error:
        raise HTTPException(status_code=500, detail="Votes could not be loaded")
    if vote is None:
        raise HTTPException(status_code=404, detail="Thread not found")
    return vote

@router.put("/threads/{thread_id}/vote")
def set_thread_vote_route(thread_id: int, request: ThreadVoteRequest, current_user: dict = Depends(get_current_user)):
    if request.direction not in (-1, 0, 1):
        raise HTTPException(status_code=422, detail="Direction must be -1, 0 or 1")

    try:
        vote = set_thread_vote(current_user["user_id"], thread_id, request.direction)
    except Error:
        raise HTTPException(status_code=500, detail="Vote could not be saved")
    if vote is None:
        raise HTTPException(status_code=404, detail="Thread not found")
    return vote

@router.post("/vote/create")
def create_follower_route(user_id: int, thread_id: int, current_user: dict = Depends(get_current_user)):
    if user_id != current_user["user_id"]:
        raise HTTPException(status_code=403, detail="Vote belongs to another user")
    try:
        vote = create_vote(user_id, thread_id)
        if not vote:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Vote could not be created")
        return vote
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.delete("/votes/delete")
def delete_vote_route(user_id: int, thread_id: int, current_user: dict = Depends(get_current_user)):
    if user_id != current_user["user_id"]:
        raise HTTPException(status_code=403, detail="Vote belongs to another user")
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
