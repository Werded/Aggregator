"""Celery app."""
import os

from celery import Celery
from celery.schedules import crontab
from kombu import Exchange, Queue

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exchange_rate_aggregator.settings")

app: Celery = Celery("Exchange Rate Aggregator")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.worker_hijack_root_logger = False
app.conf.task_ignore_result = True
app.conf.task_store_errors_even_if_ignored = True
app.conf.worker_max_memory_per_child = 200000

app.conf.task_queues = (
    Queue("high", Exchange("high"), routing_key="high"),
    Queue("normal", Exchange("normal"), routing_key="normal"),
    Queue("low", Exchange("low"), routing_key="low"),
)

app.conf.task_default_queue = "normal"
app.conf.task_default_exchange = "normal"
app.conf.task_default_routing_key = "normal"


app.conf.task_routes = {
    "exchange_rate_aggregator.checker.tasks.check_belarus_bank_rates": {
        "queue": "normal"
    },
}
app.conf.beat_schedule = {
    "check": {
        "task": "exchange_rate_aggregator.checker.tasks.check_belarus_bank_rates",
        # Execute every hour
        "schedule": crontab(hour="*/1"),
    }
}
