from app.services.hindsight.recall import recall_memories
from app.services.hindsight.retain import retain_memory
from app.services.llm_service import llm_service
from app.utils.memory_formatter import format_memories_for_prompt
from app.utils.memory_ranking import rank_memories
from app.prompts.system.support_agent_prompt import get_system_prompt
from app.core.logging import logger

class AgentService:
    async def process_message(self, customer_id: str, user_message: str, recall_limit: int = None) -> dict:
        # 1. Recall relevant memories from Hindsight
        raw_memories = await recall_memories(customer_id, user_message, limit=recall_limit)
        # 2. Rank memories by relevance (score)
        ranked_memories = rank_memories(raw_memories, limit=recall_limit or 5)
        # 3. Format memories for LLM prompt
        memories_text = format_memories_for_prompt(ranked_memories)

        # 4. Generate response from LLM
        system_prompt = get_system_prompt()
        assistant_reply = await llm_service.generate(system_prompt, user_message, memories_text)

        # 5. Store the new interaction in Hindsight memory
        metadata = {
            "timestamp": "now",  # actual timestamp can be added
            "customer_id": customer_id
        }
        memory_id = await retain_memory(customer_id, user_message, assistant_reply, metadata)

        # 6. Return result with telemetry data
        return {
            "reply": assistant_reply,
            "recalled_count": len(ranked_memories),
            "memory_id": memory_id
        }

agent_service = AgentService()