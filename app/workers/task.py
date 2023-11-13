from app.core.celery_app import celery_app


@celery_app.task(name="celery_task")
def celery_task(name: str):
    print("hello " + name)
