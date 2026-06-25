from fastapi import Depends
from backend.app.services.lastfm import LastFMService
from backend.app.lifespan import get_global_http_client
from backend.app.services.comparison import ComparisonService

def get_lastfm_service():
    return LastFMService(get_global_http_client())


def get_comparison_service(lastfm: LastFMService = Depends(get_lastfm_service)):
    return ComparisonService(lastfm)