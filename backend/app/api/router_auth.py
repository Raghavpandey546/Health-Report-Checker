from fastapi import APIRouter

router = APIRouter()

@router.get("/hello-auth")
def hello_auth():
    """
    A simple test endpoint for the auth router.
    """
    return {"message": "Hello from the auth router!"}
