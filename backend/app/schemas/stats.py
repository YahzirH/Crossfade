from pydantic import BaseModel

class UserStats(BaseModel):
    username: str
    playcount: int
    artist_count: int
    track_count: int
    album_count: int