from app.services.base import BaseService
from app.schemas.sale import SaleCreate, SaleUpdate
from app.core.config import settings


class SaleService(BaseService[SaleCreate, SaleUpdate]):
    ...


sale_service = SaleService(settings.DATABASE_URL + '/sale')