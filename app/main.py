from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.middleware.request_tracker import request_tracker_middleware
from app.core.logging import setup_logging
from app.database.connection import engine, Base

# Setup logging
setup_logging()

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="Customer Support Agent with Hindsight",
    description="AI-powered customer support agent with persistent memory using Hindsight",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom middleware
app.middleware("http")(request_tracker_middleware)

# Include API routes
app.include_router(api_router)

@app.get("/")
def root():
    return {
        "message": "Customer Support Agent with Hindsight Memory",
        "docs": "/docs",
        "health": "/api/v1/health/"
    }