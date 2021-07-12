from django.core.files.storage import default_storage

from ..celeryconf import app
from .management.commands.delete_event_payloads import delete_event_payloads


@app.task
def delete_from_storage_task(path):
    default_storage.delete(path)


@app.task
def delete_event_payloads_task():
    delete_event_payloads()
