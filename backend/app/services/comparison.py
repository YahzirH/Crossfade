import logging
from backend.app.schemas.comparison import UserComparison

# Initialize a logger for this module
logger = logging.getLogger(f"crossfade.{__name__}")

class ComparisonService:
    def __init__(self, lastfm_service):
        self.lastfm = lastfm_service

    # Compute the Jaccard similarity between two lists
    def _jaccard_similarity(self, list1, list2):
        intersection = len(set(list1) & set(list2))
        union = len(set(list1) | set(list2))

        if union == 0:
            return 0.0

        return intersection / union
    
    async def compare_users(self, user1, user2):
        logger.info(f"Comparing users: {user1} and {user2}")

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
        logger.info(f"Shared artists: {len(shared_artists)}, Shared tracks: {len(shared_tracks)}")

        # Calculate Jaccard similarity scores for artists and tracks
        artist_score = self._jaccard_similarity(user_a["artists"], user_b["artists"])
        track_score = self._jaccard_similarity(user_a["tracks"], user_b["tracks"])
        logger.info(f"Artist score: {artist_score}, Track score: {track_score}")

        return {
            "user_a": user_a["name"],
            "user_b": user_b["name"],
            "shared_artists": shared_artists,
            "shared_tracks": shared_tracks,
            "artist_score": artist_score,
            "track_score": track_score,
            "overall_score": (artist_score + track_score) / 2 
            }