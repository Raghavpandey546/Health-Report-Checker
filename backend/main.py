from fastapi import FastAPI
from app.api import router_auth
from app.db import models
from app.db.database import engine

app = FastAPI(
    title="DiagnoVerse API",
    description="Backend for the DiagnoVerse health insight platform.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    """
    The main "Hello World" endpoint.
    """
    return {"message": "Welcome to the DiagnoVerse API!"}


app.include_router(
    router_auth.router,  # The router object from our router_auth.py file
    prefix="/auth",      # A "prefix" for all URLs in that router
    tags=["Authentication"] # A tag for organizing our docs
)

models.Base.metadata.create_all(bind=engine)