from llm_cliente import gerar_resposta
import json

CATEGORIAS = ["Suporte", "Vendas", "Financeiro", "Geral"]


def classificar_mensagem(mensagem, temperature=0.2):
    prompt = f"""
    Classifique a mensagem abaixo em uma das seguintes categorias: {', '.join(CATEGORIAS)}.
    Retorne apenas um JSON no formato:
    {{
        "categoria": "nome_categoria"
    }}

    Mensagem: "{mensagem}"
    """

    resposta = gerar_resposta(prompt, temperature)

    # 1️⃣ Tentar converter para JSON
    try:
        dados = json.loads(resposta)
    except json.JSONDecodeError:
        raise ValueError("A resposta do modelo não é um JSON válido.")

    # 2️⃣ Verificar se contém a chave categoria
    if "categoria" not in dados:
        raise ValueError("O JSON não contém o campo 'categoria'.")

    categoria = dados["categoria"]

    # 3️⃣ Validar se a categoria está na lista permitida
    if categoria not in CATEGORIAS:
        raise ValueError(f"Categoria inválida retornada pelo modelo: {categoria}")

    return dados
