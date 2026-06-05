def get_sentiment_prompt() -> str:
    return """Analyze the sentiment of the following customer message. Return only one word: 'positive', 'neutral', or 'negative'.
"""