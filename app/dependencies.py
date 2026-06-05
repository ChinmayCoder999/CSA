from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.services.hindsight.client import get_hindsight_client
from app.repositories.customer_repository import CustomerRepository

# Database session dependency
def get_database_session() -> Session:
    """Yield a SQLAlchemy session, closes it when done."""
    db = get_db()
    try:
        yield db
    finally:
        db.close()

# Hindsight client dependency
def get_memory_client():
    """Return the singleton Hindsight client."""
    return get_hindsight_client()

# Customer repository dependency (optional convenience)
def get_customer_repository(db: Session = Depends(get_database_session)):
    """Provide a CustomerRepository instance."""
    return CustomerRepository(db)

# Customer resolver (creates if not exists – suitable for hackathon demo)
async def get_current_customer(
    customer_id: str,
    db: Session = Depends(get_database_session)
):
    """Fetch or create a customer by ID. Always returns a valid customer."""
    repo = CustomerRepository(db)
    customer = repo.get_or_create(customer_id)  # never returns None
    return customer