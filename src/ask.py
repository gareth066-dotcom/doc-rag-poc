from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

content = open(
    "extracted/content.txt",
    encoding="utf-8"
).read()

question = input("Question: ")

response = client.responses.create(
    model="gpt-5",
    input=f"""
Document:

{content}

Question:
{question}
"""
)

print(response.output_text)