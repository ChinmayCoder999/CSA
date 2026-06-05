from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class ChatRequest(BaseModel):
    customer_id: str
    message: str
    ticket_id: Optional[str] = None
    recall_limit: Optional[int] = None

class ChatResponse(BaseModel):
    reply: str
    recalled_memories_count: int
    telemetry: Dict[str, Any] = {}

class MemoryEntry(BaseModel):
    id: str
    text: str
    metadata: Dict[str, Any]
    score: Optional[float] = None

class HealthResponse(BaseModel):
    status: str
    hindsight_connected: bool
    groq_available: bool