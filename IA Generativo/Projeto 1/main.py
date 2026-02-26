import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)

resposta = client.chat.completions.create(
    model="llama-3.1-8b-instant",  # teste esse primeiro
    messages=[
        {"role": "user", "content": "Explique IA Generativa em 2 parágrafos."}
    ],
)

print(resposta.choices[0].message.content)
