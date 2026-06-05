from typing import List, Dict, Any

def rank_memories(memories: List[Dict[str, Any]], limit: int = 5) -> List[Dict[str, Any]]:
    """Rank memories by relevance score (higher is better) and return top `limit`."""
    def relevance_key(mem):
        # Use 'score' if present, else 0.0
        return mem.get("score", 0.0)

    ranked = sorted(memories, key=relevance_key, reverse=True)
    return ranked[:limit]