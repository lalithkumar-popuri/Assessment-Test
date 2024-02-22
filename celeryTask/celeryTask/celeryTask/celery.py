from __future__ import absolute_import,unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryTask.settings')

app = Celery('celeryTask')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    "scrap_proxy" : {
        'task' : 'taskApp.tasks.scrape_proxy_data',
        'schedule' : crontab(hour = 8, minute=44),
    }
}

app.autodiscover_tasks()

@app.task(bind = True)
def debug_task(self):
    print(f"request:{self.request!r}")