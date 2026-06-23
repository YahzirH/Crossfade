from contextlib import asynccontextmanager
import httpx 
from fastapi import FastAPI

_http_client: httpx.AsyncClient | None = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global _http_client
    _http_client = httpx.AsyncClient(base_url="http://ws.audioscrobbler.com/2.0/")
    yield
    await _http_client.aclose()

def get_global_http_client() -> httpx.AsyncClient:
    if _http_client is None:
        raise RuntimeError("HTTPX client has not been initialized via lifespan.")
    return _http_client