from fastapi import FastAPI 
from lifespan import lifespan
from routers.lastfm import router as lastfm_router

app = FastAPI(lifespan=lifespan)

# Register the routes from the router file
app.include_router(lastfm_router)