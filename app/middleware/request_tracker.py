from fastapi import Request
import time
from app.core.logging import logger

async def request_tracker_middleware(request: Request, call_next):
    """Log request method, path, and duration for every incoming request."""
    start = time.time()
    response = await call_next(request)
    duration = (time.time() - start) * 1000
    logger.info(f"{request.method} {request.url.path} completed in {duration:.2f}ms")
    response.headers["X-Response-Time-ms"] = str(int(duration))
    return response