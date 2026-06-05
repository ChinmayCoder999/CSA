from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from app.database import models
from typing import Optional

class TicketRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_ticket(self, ticket_id: str, customer_id: str, summary: str = None) -> models.Ticket:
    # Check if ticket already exists
        existing = self.db.query(models.Ticket).filter(models.Ticket.ticket_id == ticket_id).first()
        if existing:
            return existing
        ticket = models.Ticket(
            ticket_id=ticket_id,
            customer_id=customer_id,
            summary=summary
        )
        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket

    def resolve_ticket(self, ticket_id: str):
        ticket = self.db.query(models.Ticket).filter(
            models.Ticket.ticket_id == ticket_id
        ).first()
        if ticket:
            ticket.status = "resolved"
            ticket.resolved_at = func.now()
            self.db.commit()

    def get_by_customer(self, customer_id: str) -> list:
        return self.db.query(models.Ticket).filter(
            models.Ticket.customer_id == customer_id
        ).all()