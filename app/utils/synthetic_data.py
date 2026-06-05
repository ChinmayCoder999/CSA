import asyncio
from app.database.connection import SessionLocal
from app.repositories.customer_repository import CustomerRepository
from app.repositories.ticket_repository import TicketRepository
from app.services.hindsight.retain import retain_memory

def generate_synthetic_customers_and_tickets(db_session):
    """Create synthetic customers and tickets in the local database."""
    customers = [
        {"customer_id": "cust_001", "company": "Acme Corp"},
        {"customer_id": "cust_002", "company": "Beta LLC"},
        {"customer_id": "cust_003", "company": "Gamma Inc"}
    ]
    cust_repo = CustomerRepository(db_session)
    ticket_repo = TicketRepository(db_session)

    for cust in customers:
        cust_repo.get_or_create(cust["customer_id"], cust["company"])
        # Create an open ticket for each customer
        ticket_repo.create_ticket(
            ticket_id=f"tkt_{cust['customer_id']}_1",
            customer_id=cust["customer_id"],
            summary="Initial support request"
        )

async def seed_hindsight_memories():
    """Seed Hindsight with synthetic conversations."""
    conversations = [
        ("cust_001", "I cannot log in after resetting my password.", 
         "I understand. Please try clearing your browser cache and using incognito mode."),
        ("cust_001", "Still not working", 
         "Let me send you a magic link to reset your password again."),
        ("cust_002", "Your API returns 500 errors on my requests", 
         "We fixed that issue in version 2.1. Please upgrade your client and try again."),
        ("cust_003", "How do I cancel my subscription?", 
         "You can cancel from the billing section. I can also help you downgrade to a free plan if you prefer.")
    ]
    for cust_id, user_msg, assistant_msg in conversations:
        retain_memory(
            customer_id=cust_id,
            user_message=user_msg,
            assistant_message=assistant_msg,
            metadata={"source": "synthetic_seed"}
        )

def seed_all():
    """Run all seeding operations."""
    db = SessionLocal()
    try:
        generate_synthetic_customers_and_tickets(db)
        print("✅ Synthetic customers and tickets created.")
    finally:
        db.close()
    
    asyncio.run(seed_hindsight_memories())
    print("✅ Hindsight memories seeded.")

if __name__ == "__main__":
    seed_all()