# Responsável por conectar com a API.
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY não encontrada no ambiente.")

client = OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1"
)


def gerar_resposta(prompt, temperature=0.2):
    resposta = client.responses.create(
        model="llama-3.1-8b-instant",
        temperature=temperature,
        input=[
            {
                "role": "system",
                "content": (
                    "Você é um classificador de mensagens. "
                    "Responda exclusivamente em JSON válido. "
                    "Não escreva explicações. "
                    "Não adicione texto fora do JSON."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return resposta.output_text.strip()
