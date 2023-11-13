from app.core.celery_app import celery_app
from app.core.config import settings

WORKER_ENVIRONMENT = "" if settings.ENVIRONMENT == "prod" else "-dev"

celery_app.send_task(
    name="celery_task", args=["name"], queue=f"worker-template-task{WORKER_ENVIRONMENT}"
)
