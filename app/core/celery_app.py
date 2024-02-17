from celery import Celery
from celery.signals import setup_logging, celeryd_after_setup

from app.core.config import settings
from app.core.logger import MyFormat, get_logger

log = get_logger(__name__)


CELERY_BROKER = f"{settings.AMQP_DSN}"
SCHEDULE_TIME = settings.SCHEDULE_TIME


WORKER_ENVIRONMENT = "" if settings.ENVIRONMENT == "prod" else "-dev"


celery_config = {
    "broker_url": CELERY_BROKER,
    "task_ignore_result": True,
    "result_expires": 7200,  # in secs
    "worker_prefetch_multiplier": 1,
}


celery_app = Celery("worker", config_source=celery_config)


celery_app.conf.task_routes = {
    "app.workers.sale.sale": {
        "queue": f"cotizadorV2-sale{WORKER_ENVIRONMENT}"
    }
}

celery_app.conf.update(
    task_track_started=True,
    accept_content=["json"],
)


@setup_logging.connect
def setup_loggers(*args, **kwargs):
    import logging

    log = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter(MyFormat())
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)


@celeryd_after_setup.connect
def start_up(*args, **kwargs):
    import logging

    log = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter(MyFormat())
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    log.info("register firebase")