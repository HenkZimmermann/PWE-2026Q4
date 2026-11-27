from fastapi import APIRouter, HTTPException, status, Depends
from src.sections.user_statistics.user_statistics_service import * 
router = APIRouter()
@router.post("/stats/{user_id}")
def login(user_id: int):
    stats = get_user_stats(user_id)
    return stats
    