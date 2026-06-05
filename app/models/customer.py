from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CustomerProfile(BaseModel):
    customer_id: str
    company: Optional[str] = None
    sentiment_score: float = 0.5
    created_at: Optional[datetime] = None