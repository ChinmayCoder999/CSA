from sqlalchemy.orm import Session
from app.database import models

class CustomerRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_or_create(self, customer_id: str, company: str = None) -> models.Customer:
        customer = self.db.query(models.Customer).filter(
            models.Customer.customer_id == customer_id
        ).first()
        if not customer:
            customer = models.Customer(customer_id=customer_id, company=company)
            self.db.add(customer)
            self.db.commit()
            self.db.refresh(customer)
        return customer

    def update_sentiment(self, customer_id: str, new_score: float):
        customer = self.db.query(models.Customer).filter(
            models.Customer.customer_id == customer_id
        ).first()
        if customer:
            customer.sentiment_score = new_score
            self.db.commit()