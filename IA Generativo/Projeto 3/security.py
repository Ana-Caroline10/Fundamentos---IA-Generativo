def detect_prompt_injection(query: str) -> bool:
    suspicious_patterns = [
        "ignore previous instructions",
        "system prompt",
        "me diga qual",
        "quais sao suas instrucoes",
        "reveal your prompt",
        "mostre o prompt"
    ]

    query_lower = query.lower()

    for pattern in suspicious_patterns:
        if pattern in query_lower:
            return True

    return False
