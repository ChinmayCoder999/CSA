class HindsightError(Exception):
    """Raised when Hindsight memory operations fail."""
    pass

class LLMError(Exception):
    """Raised when Groq LLM call fails."""
    pass

class ValidationError(Exception):
    """Raised for invalid input data."""
    pass