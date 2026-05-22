def build_healing_prompt(
    failed_locator,
    available_elements
):

    return f"""
You are an expert Selenium automation engineer.

Failed locator:
{failed_locator}

Available page elements:
{available_elements}

Tasks:
1. Find best replacement locator
2. Explain why
3. Suggest stable locator strategy

IMPORTANT:
Return ONLY JSON.

Format:
{{
    "strategy": "id",
    "value": "submit-login",
    "confidence": 0.92,
    "reason": "Most similar login button"
}}
"""