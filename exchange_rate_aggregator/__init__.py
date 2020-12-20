from typing import List

from exchange_rate_aggregator.celery import app as celery_app

__version__: str = "0.0.1"
__all__: List[str] = [
    "__version__",
    "celery_app",
]
