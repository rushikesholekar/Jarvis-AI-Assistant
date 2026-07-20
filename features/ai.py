from urllib import response

from app.config import AI_MODEL, MAX_HISTORY
from ollama import chat
from app.logger import log
import json
import time
import re


messages = [
    {
        "role": "system",
        "content": (
            "You are Jarvis, a helpful AI voice assistant. "
            "Give short, clear answers in 2 to 4 sentences. "
            "If the user asks for a detailed explanation, then provide one."
        )
    }
]

def ask_ai(question):
    start = time.time()

    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    response = chat(
        model=AI_MODEL,
        messages=messages
    )

    answer = response.message.content

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    if len(messages) > MAX_HISTORY + 1:
        messages[:] = [messages[0]] + messages[-MAX_HISTORY:]

    end = time.time()
    
    print(f"{answer}")

    print(f"AI took {end-start:.2f} seconds")

    return answer

def parse_json_response(text):
    match = re.search(r"\{.*?\}", text, re.DOTALL)

    if not match:
        return {}

    try:
        return json.loads(match.group())
    except json.JSONDecodeError:
        return {}

def extract_memory(text):
    system_prompt = """
   You are an information extraction AI.

   IMPORTANT RULES:

1. Never answer the user's question.
2. Never use your own knowledge.
3. Never infer missing information.
4. Only extract information that the USER explicitly says about themselves.
5. Never save information about other people, companies, programming languages, YouTube channels, books, or general knowledge.
6. If the user is asking a question, reply ONLY with:

{}

Your only job is to extract ONE personal fact from the user's sentence.

If the sentence contains a personal fact, reply ONLY with valid JSON in this format:

{
    "key": "...",
    "value": "..."
}

Examples:

User: I live in Mumbai.
Output:
{"key":"location","value":"Mumbai"}

User: My birthday is 23rd October.
Output:
{"key":"birthday","value":"23rd October"}

User: I am learning Python.
Output:
{"key":"learning","value":"Python"}

User: I study Information Technology.
Output:
{"key":"education","value":"Information Technology"}

User: My favourite game is Call of Duty.
Output:
{"key":"favourite game","value":"Call of Duty"}

User: I want to become a product based software engineer.
Output:
{"key":"goal","value":"product based software engineer"}

User: Who created Python?
Output:
{}

User: When was Guido van Rossum born?
Output:
{}

User: Tell me about Python.
Output:
{}

User: What is Artificial Intelligence?
Output:
{}

User: Who owns Microsoft?
Output:
{}

User: Do you know CodeWithHarry?
Output:
{}

User: Where was Albert Einstein born?
Output:
{}

User: My favorite editor is VS Code.
Output:
{"key":"favorite editor","value":"VS Code"}

If the sentence contains no personal information, reply ONLY with:

{}

CRITICAL:

Your entire reply must contain EXACTLY ONE valid JSON object.

Never output explanations.

Never output multiple JSON objects.

Never output alternatives.

Never output "OR".

Never output text before or after the JSON.

Your reply must begin with { and end with }.

Any other response is incorrect.
    """
    memory_messages = [
    {
        "role": "system",
        "content": system_prompt
    },
    {
        "role": "user",
        "content": text
    }
    ]
    response = chat(
        model=AI_MODEL,
        messages=memory_messages
    )
    try:
        print(response.message.content)

        data = parse_json_response(response.message.content)

        return data
    
    except Exception as e:
        log(f"Memory extraction error: {e}")
        return {}

