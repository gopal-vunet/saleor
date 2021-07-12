import datetime

from django.core.management.base import BaseCommand

from ....settings import EVENT_PAYLOAD_DELETE_PERIOD
from ...models import EventPayload, EventTask


def delete_event_payloads():
    event_payload_delete_period = (
        datetime.datetime.today() - EVENT_PAYLOAD_DELETE_PERIOD
    )

    EventTask.objects.filter(created_at__lte=event_payload_delete_period).delete()

    EventPayload.objects.filter(event_tasks__isnull=True).delete()


class Command(BaseCommand):
    help = (
        "Delete EventPayloads and EventTasks from database "
        "that are older than the value set "
        "in EVENT_PAYLOAD_DELETE_PERIOD environment variable."
    )

    def handle(self, **options):
        delete_event_payloads()
