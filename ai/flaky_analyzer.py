from ai.flaky_prompt import build_flaky_prompt
from ai.openai_client import ask_openai


def analyze_flaky_test(error_details):

    prompt = build_flaky_prompt(error_details)

    analysis = ask_openai(prompt)

    return analysis