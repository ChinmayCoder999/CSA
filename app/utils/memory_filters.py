from typing import List, Dict, Any

def filter_by_ticket_status(memories: List[Dict[str, Any]], only_open_tickets: bool = True) -> List[Dict[str, Any]]:
    """Filter memories to exclude those associated with resolved tickets (if metadata present)."""
    if not only_open_tickets:
        return memories
    filtered = []
    for mem in memories:
        metadata = mem.get("metadata", {})
        ticket_status = metadata.get("ticket_status", "")
        if ticket_status != "resolved":
            filtered.append(mem)
    return filtered