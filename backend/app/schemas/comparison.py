from pydantic import BaseModel

class UserComparison(BaseModel):
    user_a: str
    user_b: str
    shared_artists: list[str]
    shared_tracks: list[str]
    artist_score: float
    track_score: float
    overall_score: float