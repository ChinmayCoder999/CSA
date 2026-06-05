import time
from typing import Optional
from app.core.metrics import metrics
from app.core.logging import logger

class Telemetry:
    """Records telemetry data for Hindsight memory operations."""

    @staticmethod
    def track_recall(customer_id: str, query: str, recall_count: int, latency_ms: float):
        """Track a recall operation."""
        metrics.recall_count += 1
        metrics.total_recall_latency_ms += latency_ms
        if recall_count > 0:
            metrics.recall_hits += 1
        logger.info(f"Recall: customer={customer_id}, query='{query[:50]}...', count={recall_count}, latency={latency_ms:.2f}ms")

    @staticmethod
    def track_retain(customer_id: str, latency_ms: float):
        """Track a retain operation."""
        metrics.retain_count += 1
        metrics.total_retain_latency_ms += latency_ms
        logger.info(f"Retain: customer={customer_id}, latency={latency_ms:.2f}ms")

# Singleton instance
telemetry = Telemetry()