from groq import Groq
from dotenv import load_dotenv
from tools import data_atual, calcular_idade, gerar_senha
import os
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

ARQUIVO_MEMORIA = "memory.json"
LIMITE_MEMORIA = 10

# Persona do assistente
PERSONA = {
    "role": "system",
    "content": "Você é um assistente virtual educado, claro e prestativo. Sempre responda de forma amigável."
}

historico_mensagens = [PERSONA]


# ==========================
# Persistência de memória
# ==========================

def carregar_memoria():
    global historico_mensagens

    if os.path.exists(ARQUIVO_MEMORIA):
        with open(ARQUIVO_MEMORIA, "r", encoding="utf-8") as f:
            historico_mensagens = json.load(f)


def salvar_memoria():
    with open(ARQUIVO_MEMORIA, "w", encoding="utf-8") as f:
        json.dump(historico_mensagens, f, indent=2, ensure_ascii=False)


# ==========================
# Controle de memória
# ==========================

def salvar_historico(mensagem):
    historico_mensagens.append(mensagem)

    # limite de memória
    if len(historico_mensagens) > LIMITE_MEMORIA:
        historico_mensagens.pop(1)  # mantém persona


# ==========================
# Tools automáticas
# ==========================

def verificar_tools(pergunta):

    pergunta_lower = pergunta.lower()

    if "data" in pergunta_lower:
        return f"Hoje é {data_atual()}"

    if "idade" in pergunta_lower:

        try:
            ano = input("Digite seu ano de nascimento: ")
            idade = calcular_idade(ano)
            return f"Você tem aproximadamente {idade} anos."
        except:
            return "Não consegui calcular a idade."

    if "senha" in pergunta_lower:
        senha = gerar_senha()
        return f"Sua senha gerada é: {senha}"

    return None


# ==========================
# Chat principal
# ==========================

def chat(pergunta):

    salvar_historico({"role": "user", "content": pergunta})

    resposta = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=historico_mensagens
    )

    resposta_conteudo = resposta.choices[0].message.content

    salvar_historico({"role": "assistant", "content": resposta_conteudo})

    salvar_memoria()

    return resposta_conteudo


# ==========================
# Programa principal
# ==========================

def main():

    carregar_memoria()

    while True:

        pergunta = input("Você: ")

        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Encerrando o chat.")
            break

        # limpar memória
        if pergunta == "/limpar":
            global historico_mensagens
            historico_mensagens = [PERSONA]
            salvar_memoria()
            print("Assistente: Memória da conversa apagada.")
            continue

        # verificar tools
        resultado_tool = verificar_tools(pergunta)

        if resultado_tool:
            salvar_historico({"role": "assistant", "content": resultado_tool})
            salvar_memoria()
            print("Assistente:", resultado_tool)
            continue

        resposta = chat(pergunta)
        print("Assistente:", resposta)


if __name__ == "__main__":
    main()
