from pydantic import BaseModel
from typing import Dict, Any, Optional

class MemoryPayload(BaseModel):
    customer_id: str
    user_message: str
    assistant_message: str
    metadata: Optional[Dict[str, Any]] = None