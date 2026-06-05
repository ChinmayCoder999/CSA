import time
from app.services.hindsight.client import get_hindsight_client
from app.core.telemetry import telemetry
from app.core.logging import logger
from app.config import settings

async def retain_memory(customer_id: str, user_message: str, assistant_message: str, metadata: dict = None):
    start = time.time()
    client = get_hindsight_client()

    try:
        content = f"User: {user_message}\nAssistant: {assistant_message}"
        # The client.retain method now only requires content and metadata
        result = await client.retain(content=content, metadata=metadata or {})
        latency_ms = (time.time() - start) * 1000
        telemetry.track_retain(customer_id, latency_ms)
        logger.debug(f"Memory retained for {customer_id}. Result: {result}")
        # The operation ID can be used to track async processing if needed
        return result.get("operation_id") or result.get("id")
    except Exception as e:
        logger.error(f"Retain failed for customer {customer_id}: {e}")
        raise