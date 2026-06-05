import asyncio
from app.database.connection import engine, Base
from app.utils.synthetic_data import generate_synthetic_customers_and_tickets

def seed_all():
    # Create all tables first
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created.")

    # Seed data
    from app.database.connection import SessionLocal
    db = SessionLocal()
    try:
        generate_synthetic_customers_and_tickets(db)
        print("✅ Synthetic customers and tickets created.")
    finally:
        db.close()

    # Skip Hindsight seeding to avoid event loop issues
    print("⚠️ Hindsight memory seeding skipped (optional). Memories will be created during live conversations.")

if __name__ == "__main__":
    seed_all()