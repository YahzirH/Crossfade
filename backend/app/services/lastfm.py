import httpx
from fastapi import Depends, HTTPException
from backend.app.core.config import settings
from backend.app.lifespan import get_global_http_client

# Load the Last.fm API key from the environment variables
LASTFM_API_KEY = settings.lastfm_api_key

class LastFMService:
    def __init__(self, http_client: httpx.AsyncClient = Depends(get_global_http_client)):
        self.client = http_client
        # Double-check that the key exists when the service boots up
        if not LASTFM_API_KEY:
            raise RuntimeError("CRITICAL: LASTFM_API_KEY environment variable is missing!")

    async def _request(self, method: str, **params):
        try:
            response = await self.client.get(
                "",
                params={
                    "method": method,
                    "api_key": LASTFM_API_KEY,
                    "format": "json",
                    **params
                }
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=e.response.status_code, 
                detail=f"Error fetching data from Last.fm method {method}"
            )
        except httpx.RequestError:
            raise HTTPException(
                status_code=503, 
                detail="Last.fm API is currently unreachable"
            )
        
    async def get_user_info(self, username: str):
        return await self._request("user.getInfo", user=username)
    
    async def get_top_artists(self, username: str, limit: int = 50):
        data = await self._request("user.getTopArtists", user=username, limit=limit)
        return [
            artist["name"] 
            for artist in data["topartists"]["artist"]
        ]
    
    async def get_top_tracks(self, username: str, limit: int = 50):
        data = await self._request("user.getTopTracks", user=username, limit=limit)
        return [
            track["name"] 
            for track in data["toptracks"]["track"]
        ]