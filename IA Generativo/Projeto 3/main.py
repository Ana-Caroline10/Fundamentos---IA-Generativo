from llm_client import LLMClient
from retriever import load_conhecimento, semantic_retriever
from validator import validate_json
from prompt import build_system_prompt
from security import detect_prompt_injection


def main():
    provider = input("Escolha o provedor (groq): ").strip().lower()
    client = LLMClient(provider=provider)

    # Carrega conhecimento e cria embeddings
    load_conhecimento()

    while True:
        query = input("Digite sua pergunta (ou 'sair' para encerrar): ").strip()

        if query.lower() == "sair":
            break

        # 🔒 Proteção contra Prompt Injection
        if detect_prompt_injection(query):
            print("Pergunta bloqueada por tentativa de prompt injection.\n")
            continue

        # 🔎 Busca semântica
        contexto = semantic_retriever(query)

        system_prompt = build_system_prompt()

        response_text = client.generate_text(system_prompt, contexto)

        if not response_text:
            print("Erro: modelo retornou resposta vazia.\n")
            continue

        is_valid, data = validate_json(response_text)

        if is_valid:
            print(f"Resposta: {data.get('resposta')}\n")
        else:
            print(f"Resposta inválida do modelo:\n{data}\n")


if __name__ == "__main__":
    main()
