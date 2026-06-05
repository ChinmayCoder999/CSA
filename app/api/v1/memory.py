from fastapi import APIRouter
from app.core.metrics import metrics

router = APIRouter(prefix="/memory", tags=["memory"])

@router.get("/metrics")
def get_memory_metrics():
    return {
        "recall_count": metrics.recall_count,
        "recall_hits": metrics.recall_hits,
        "recall_hit_rate": metrics.recall_hit_rate,
        "avg_recall_latency_ms": metrics.avg_recall_latency_ms,
        "retain_count": metrics.retain_count,
        "avg_retain_latency_ms": metrics.avg_retain_latency_ms,
    }