import httpx
from app.config import settings
from app.core.logging import logger


class HindsightAsyncClient:
    def __init__(self):
        self.base_url = settings.hindsight_base_url.rstrip("/")
        self.api_key = settings.hindsight_api_key
        self.namespace = settings.hindsight_namespace
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def _get_bank_id(self) -> str:
        """Return the bank ID (same as namespace for cloud)."""
        return self.namespace

    async def recall(self, query: str, limit: int = 5) -> list:
        """Recall memories using the correct API path."""
        bank_id = self._get_bank_id()
        url = f"{self.base_url}/v1/default/banks/{bank_id}/memories/recall"

        payload = {
            "query": query,
            "max_tokens": 4096,
            "budget": "mid",
        }

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                url,
                headers=self.headers,
                json=payload,
            )

            if response.status_code == 404:
                logger.error(f"Endpoint not found. Check your API URL: {url}")
                raise Exception(f"API endpoint not found: {url}")

            response.raise_for_status()
            data = response.json()

            if isinstance(data, dict):
                return data.get("results", [])

            return []

    async def retain(self, content: str, metadata: dict = None) -> dict:
        """Retain a memory using the correct API path."""
        bank_id = self._get_bank_id()
        url = f"{self.base_url}/v1/default/banks/{bank_id}/memories/retain"

        payload = {
            "items": [
                {
                    "content": content,
                    "metadata": metadata or {},
                }
            ],
            "async": False,
        }

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                url,
                headers=self.headers,
                json=payload,
            )

            if response.status_code >= 400:
                logger.warning(
                    f"Retain skipped: {response.status_code} - {response.text}"
                )
                return {"status": "skipped"}

            return response.json()


# Singleton instance
_hindsight_client = None


def get_hindsight_client() -> HindsightAsyncClient:
    global _hindsight_client

    if _hindsight_client is None:
        _hindsight_client = HindsightAsyncClient()

    return _hindsight_client