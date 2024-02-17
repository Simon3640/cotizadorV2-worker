from enum import Enum

from pydantic import BaseModel



class SaleStatus(str, Enum):
    PRICE = "cotización"
    PAID = "pagada"
    CANCELLED = "cancelado"
    REMISSION = "remisión"


class SaleBase(BaseModel):
    user_id: int
    buyer_id: int
    status: SaleStatus | None = SaleStatus.PRICE


class SaleCreate(SaleBase):
    ...


class SaleUpdate(BaseModel):
    user_id: int | None
    buyer_id: int | None
    status: SaleStatus | None
    consecutive: int | None
    document: str | None


class SaleInDB(SaleBase):
    consecutive: int | None
    document: str | None


class SaleProducts(BaseModel):
    product_id: int
    total: int
    tax: int

