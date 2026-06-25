from backend.app.schemas.comparison import UserComparison

class ComparisonService:
    def __init__(self, lastfm_service):
        self.lastfm = lastfm_service

    async def compare_users(self, user1, user2):

        artists_a = await self.lastfm.get_top_artists(user1)
        artists_b = await self.lastfm.get_top_artists(user2)

        tracks_a = await self.lastfm.get_top_tracks(user1)
        tracks_b = await self.lastfm.get_top_tracks(user2)

        user_a = {
            "name": user1,
            "artists": artists_a,
            "tracks": tracks_a
        }

        user_b = {
            "name": user2,
            "artists": artists_b,
            "tracks": tracks_b
        }
        
        diff = self._compute(user_a, user_b)
        return UserComparison(**diff)
    
    def _compute(self, user_a, user_b):
        shared_artists = list(
            set(user_a["artists"]) & set(user_b["artists"])
        )

        shared_tracks = list(
            set(user_a["tracks"]) & set(user_b["tracks"])
        )

        return {
            "user_a": user_a["name"],
            "user_b": user_b["name"],
            "shared_artists": shared_artists,
            "shared_tracks": shared_tracks,
            "overall_score": 0.5
        }