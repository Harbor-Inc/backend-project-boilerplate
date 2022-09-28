from fastapi import APIRouter

from app.api.endpoints import sample

api_router = APIRouter()
api_router.include_router(sample.router, prefix="/sample", tags=["sample"])
