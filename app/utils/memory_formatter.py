from typing import List, Dict, Any

def format_memories_for_prompt(memories: List[Dict[str, Any]]) -> str:
    """Convert a list of memory objects into a formatted string for the LLM prompt."""
    if not memories:
        return "No previous interactions found for this customer."

    formatted = "Previous support interactions with this customer:\n"
    for idx, mem in enumerate(memories, 1):
        # Extract content; handle both 'content' and 'text' fields
        content = mem.get("content") or mem.get("text", "")
        formatted += f"{idx}. {content}\n"
    return formatted