import requests

from celery.task import task
from django.conf import settings


@task(name="send_email")
def send_email(self, data: dict) -> None:
    """Execute send email action"""
    requests.post(settings.MESSAGE_URL, data=data)

