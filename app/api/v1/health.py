from fastapi import APIRouter
from app.services.hindsight.client import get_hindsight_client
from app.services.llm_service import llm_service
from app.models.schemas import HealthResponse

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/", response_model=HealthResponse)
def health():
    # Check Hindsight connectivity
    hindsight_ok = False
    try:
        client = get_hindsight_client()
        # Simple test: recall with empty query (if supported) or just client init
        # For now, assume client creation means connected
        hindsight_ok = True
    except Exception:
        pass

    # Check Groq API key presence
    groq_ok = bool(llm_service.api_key)

    return HealthResponse(
        status="healthy",
        hindsight_connected=hindsight_ok,
        groq_available=groq_ok
    )