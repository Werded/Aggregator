"""Checker app tasks"""
from exchange_rate_aggregator.celery import app
from exchange_rate_aggregator.checker.clients import BelarusBankClient
from exchange_rate_aggregator.checker.clients.base import ClientException
from exchange_rate_aggregator.checker.services import CheckerService


@app.task(autoretry_for=(ClientException,), retry_kwargs={"max_retries": 3})
def check_belarus_bank_rates():
    """Task for checking BelarusBank rates"""
    service = CheckerService(BelarusBankClient)
    service.check_rates()
