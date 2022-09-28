from decimal import Decimal
from sqlalchemy.orm import Session

from app.crud.crud_product import product as crud

from app.schemas.product import ProductCreate
from app.db import base  # noqa: F401


def init_db(db: Session) -> None:
    pass
    # noqa: F841
