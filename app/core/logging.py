import logging
from app.config import settings

def setup_logging():
    """Configure logging for the entire application."""
    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

# Root logger instance
logger = logging.getLogger("hindsight_agent")