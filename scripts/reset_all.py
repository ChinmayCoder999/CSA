import os
from app.database.connection import engine, Base

def reset_database():
    """Drop all tables and recreate them (clears all local data)."""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("✅ Database reset (all tables dropped and recreated).")

if __name__ == "__main__":
    reset_database()
    print("Reset complete. You can now run `python scripts/seed.py` to populate with synthetic data.")