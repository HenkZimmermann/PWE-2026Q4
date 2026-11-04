from fastapi import APIRouter, HTTPException, status
from src.sections.follows.follows_service import *
router = APIRouter()
@router.post("/follows/create")
def create_follower_route(user_id: int, followed_user_id: int):
    try:
        follower = create_follower(user_id, followed_user_id)
        if not follower:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Follower could not be created")
        return follower
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.delete("/follows/delete")
def delete_follower_route(user_id: int, followed_user_id: int):
    try:
        result = delete_follower(user_id, followed_user_id)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Follower not found")
        return {"message": "Follower deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.get("/follows/followers/{user_id}")
def get_all_followers_of_user_id_route(user_id: int):
    try:
        followers = get_all_followers_of_user_id(user_id)
        if not followers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Followers not found")
        return followers
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.get("/follows/following/{user_id}")
def get_all_users_user_id_follows_route(user_id: int):
    try:
        follows = get_all_users_user_id_follows(user_id)
        if not follows:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Follows not found")
        return follows
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))