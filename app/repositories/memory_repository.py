from sqlalchemy.orm import Session
from app.database import models
from typing import Optional

class MemoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def log_conversation(
        self,
        customer_id: str,
        user_message: str,
        assistant_message: str,
        ticket_id: Optional[str] = None,
        hindsight_memory_id: Optional[str] = None
    ):
        """Store a conversation turn in the database."""
        log_entry = models.ConversationLog(
            customer_id=customer_id,
            ticket_id=ticket_id,
            user_message=user_message,
            assistant_message=assistant_message,
            hindsight_memory_id=hindsight_memory_id
        )
        self.db.add(log_entry)
        self.db.commit()