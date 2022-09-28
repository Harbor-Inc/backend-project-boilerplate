from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps


router = APIRouter()

@router.get("/",)
def read_sample(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve items.
    """
