import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()
from Book_Lending_App.models import BookLending
from celery import shared_task
from datetime import date, timedelta
from django.db import transaction

import logging

logger = logging.getLogger(__name__)



@shared_task
def update_fines_task():
    with transaction.atomic():
        logger.info("Task started")
        current_date = date.today()

        overdue_books = BookLending.objects.filter(due_date__lt=current_date)
        for book in overdue_books:
            book.fine += 10
            book.save()
