import httpx
from app.config import settings
from app.core.exceptions import LLMError
from app.core.logging import logger

class LLMService:
    def __init__(self):
        self.api_key = settings.groq_api_key
        self.model = settings.groq_model
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"

    async def generate(self, system_prompt: str, user_message: str, memories_text: str) -> str:
        """Generate a response from Groq with system prompt, memories, and user message."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        # Build messages
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Previous interactions:\n{memories_text}\n\nCurrent message: {user_message}"}
        ]
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.3,
            "max_tokens": 500
        }
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(self.api_url, headers=headers, json=payload)
                response.raise_for_status()
                data = response.json()
                reply = data["choices"][0]["message"]["content"]
                logger.debug(f"LLM generated response: {reply[:100]}...")
                return reply
        except Exception as e:
            logger.error(f"LLM call failed: {e}")
            raise LLMError(f"Groq API error: {str(e)}")

llm_service = LLMService()