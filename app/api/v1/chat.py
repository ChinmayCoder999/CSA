from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.services.agent_service import agent_service
from app.models.schemas import ChatRequest, ChatResponse
from app.repositories.memory_repository import MemoryRepository
from app.core.metrics import metrics
from app.core.logging import logger

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest, db: Session = Depends(get_db)):
    try:
        logger.info(f"Chat request for customer: {request.customer_id}")

        # Process the message through the agent
        result = await agent_service.process_message(
            customer_id=request.customer_id,
            user_message=request.message,
            recall_limit=request.recall_limit
        )

        # Log the conversation turn to the local database
        memory_repo = MemoryRepository(db)
        memory_repo.log_conversation(
            customer_id=request.customer_id,
            user_message=request.message,
            assistant_message=result["reply"],
            ticket_id=request.ticket_id,
            hindsight_memory_id=result.get("memory_id")
        )

        # Return response with telemetry
        return ChatResponse(
            reply=result["reply"],
            recalled_memories_count=result["recalled_count"],
            telemetry={
                "recall_hit_rate": metrics.recall_hit_rate,
                "avg_recall_latency_ms": metrics.avg_recall_latency_ms,
                "avg_retain_latency_ms": metrics.avg_retain_latency_ms
            }
        )
    except Exception as e:
        logger.error(f"Chat endpoint error: {e}")
        raise HTTPException(status_code=500, detail=str(e))