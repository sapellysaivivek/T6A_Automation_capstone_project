import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def get_client():

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY not found. "
            "Check your .env file."
        )

    return OpenAI(
        api_key=api_key
    )


def ask_openai(prompt):

    client = get_client()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content