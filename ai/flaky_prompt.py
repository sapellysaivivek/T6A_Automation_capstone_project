def build_flaky_prompt(error_details):

    return f"""
You are an expert QA Automation Engineer.

Analyze this Selenium failure.

Tasks:
1. Root cause
2. Is it flaky?
3. Retry recommendation
4. Suggested fix
5. Prevention strategy

Failure:
{error_details}

Return bullet points.
"""