from fastapi import FastAPI 
from .lifespan import lifespan
from backend.app.routers.lastfm import router as lastfm_router
from backend.app.routers.comparison import router as comparison_router

app = FastAPI(lifespan=lifespan)

# Register the routes from the router directory
app.include_router(lastfm_router)
app.include_router(comparison_router)