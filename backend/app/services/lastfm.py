import os
import httpx
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from backend.app.lifespan import get_global_http_client

# Load environment variables from .env file
load_dotenv()
# Get the Last.fm API key from environment variables
LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")

class LastFMService:
    def __init__(self, http_client: httpx.AsyncClient = Depends(get_global_http_client)):
        self.client = http_client
        # Double-check that the key exists when the service boots up
        if not LASTFM_API_KEY:
            raise RuntimeError("CRITICAL: LASTFM_API_KEY environment variable is missing!")

    async def get_user_info(self, username: str):
        try:
            response = await self.client.get("", params={
                "method": "user.getinfo",
                "user": username,
                "api_key": LASTFM_API_KEY,
                "format": "json"
            })
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=e.response.status_code, 
                detail="Error fetching user info from Last.fm"
                )
        except httpx.RequestError:
            raise HTTPException(
                status_code=503, 
                detail="Last.fm API is currently unreachable"
            )