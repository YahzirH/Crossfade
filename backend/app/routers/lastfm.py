from fastapi import APIRouter, Depends
from backend.app.services.lastfm import LastFMService

router = APIRouter(prefix="/lastfm", tags=["lastfm"])

@router.get("/user/{username}")
async def get_user_info(username: str, service: LastFMService = Depends()):
    return await service.get_user_info(username)