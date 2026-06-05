from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Ticket(BaseModel):
    ticket_id: str
    customer_id: str
    status: str = "open"   # open, resolved, closed
    summary: Optional[str] = None
    resolved_at: Optional[datetime] = None
    created_at: Optional[datetime] = None