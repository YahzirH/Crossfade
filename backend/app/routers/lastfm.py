from fastapi import APIRouter, Depends
from backend.app.services.lastfm import LastFMService
from backend.app.schemas.stats import UserStats

router = APIRouter(prefix="/lastfm", tags=["lastfm"])

@router.get("/user/{username}", response_model=UserStats)
async def get_user_info(username: str, service: LastFMService = Depends()):
    data = await service.get_user_info(username)

    user = data["user"]

    return UserStats(
        username=user["name"],
        playcount=int(user["playcount"]),
        artist_count=int(user["artist_count"]),
        track_count=int(user["track_count"]),
        album_count=int(user["album_count"]),
    )