import time
from app.services.hindsight.client import get_hindsight_client
from app.core.telemetry import telemetry
from app.core.logging import logger
from app.config import settings

async def recall_memories(customer_id: str, query: str, limit: int = None) -> list:
    start = time.time()
    if limit is None:
        limit = settings.default_recall_limit
    limit = min(limit, settings.max_recall_limit)

    client = get_hindsight_client()

    try:
        # The client.recall method now only requires the query
        results = await client.recall(query=query, limit=limit)
        latency_ms = (time.time() - start) * 1000
        recall_count = len(results)
        telemetry.track_recall(customer_id, query, recall_count, latency_ms)
        logger.debug(f"Recalled {recall_count} memories for {customer_id}")
        return results
    except Exception as e:
        logger.error(f"Recall failed for customer {customer_id}: {e}")
        return []