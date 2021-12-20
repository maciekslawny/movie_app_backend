from celery import shared_task
from movies_app.services import update_db


@shared_task
def fetch_data_from_api():
    update_db()
