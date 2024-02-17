from app.core.celery_app import celery_app
from app.core.config import settings
from app.workers.sale import sale

WORKER_ENVIRONMENT = "" if settings.ENVIRONMENT == "prod" else "-dev"


sale(9)

# celery_app.send_task(
#     name="sale", args=[1], queue=f"cotizadorV2-sale{WORKER_ENVIRONMENT}"
# )
