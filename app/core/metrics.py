class Metrics:
    """Central store for memory operation metrics."""

    def __init__(self):
        self.recall_count = 0
        self.recall_hits = 0          # number of recalls that returned at least one memory
        self.total_recall_latency_ms = 0.0
        self.retain_count = 0
        self.total_retain_latency_ms = 0.0

    @property
    def avg_recall_latency_ms(self) -> float:
        """Average latency of recall operations in milliseconds."""
        if self.recall_count == 0:
            return 0.0
        return self.total_recall_latency_ms / self.recall_count

    @property
    def recall_hit_rate(self) -> float:
        """Proportion of recall operations that returned at least one memory."""
        if self.recall_count == 0:
            return 0.0
        return self.recall_hits / self.recall_count

    @property
    def avg_retain_latency_ms(self) -> float:
        """Average latency of retain operations in milliseconds."""
        if self.retain_count == 0:
            return 0.0
        return self.total_retain_latency_ms / self.retain_count

# Singleton instance
metrics = Metrics()