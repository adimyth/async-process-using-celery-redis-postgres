import os

from celery import Celery
from dotenv import load_dotenv

load_dotenv()

app = Celery("celery-app", broker=os.getenv("CELERY_BROKER_URL"))

# Configure the Celery app to use the Postgres adapter
app.conf.update(
    result_backend=os.getenv("CELERY_RESULT_BACKEND"),
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="Asia/Kolkata",
    enable_utc=True,
    include=["celery_app.tasks"],
)
