from app.core.celery_app import celery_app
from app.services.sale import sale_service
from app.services.jinja2.sale import generate_pdf
from app.schemas.sale import SaleUpdate


@celery_app.task(name="sale")
def sale(id: int):
    sale = sale_service.get_byid(id=id)

    path = generate_pdf(sale)

    update = {"document": path}

    sale_service.update(id=id, obj_in=update, route="/worker")
    
