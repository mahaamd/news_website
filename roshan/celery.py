import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roshan.settings')

app = Celery('roshan')

# Load task modules from all registered Django apps.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
