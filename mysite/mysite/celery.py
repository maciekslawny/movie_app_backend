import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

app = Celery("mysite")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "add-every-day-10-am": {
        "task": "movies_app.tasks.fetch_data_from_api",
        "schedule": crontab(hour=11, minute=44),
    }
}

app.conf.timezone = "UTC"

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
