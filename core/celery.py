import os
from celery import Celery
from .tasks import update_fines_task
from django.conf import settings

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Create an instance of the Celery app
app = Celery('core')

# Load the celery configuration from the Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks in all registered Django app configs
app.autodiscover_tasks()