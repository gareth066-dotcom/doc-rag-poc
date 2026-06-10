from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from retrieve import load_relevant_context

load_dotenv()

client = OpenAI()
content_path = Path("extracted/content.txt")

while True:

    question = input("\nQuestion: ")

    if question.lower() == "exit":
        break

    context = load_relevant_context(content_path, question)

    response = client.responses.create(
        model="gpt-5",
        input=f"""
You are a document assistant.

Answer only from the provided content.
If the answer is not in the excerpts, say you could not find it.

DOCUMENT EXCERPTS:

{context}

QUESTION:

{question}
"""
    )

    print("\nAnswer:")
    print(response.output_text)