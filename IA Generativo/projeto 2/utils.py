import json

def parse_json_resposta(resposta_str):
    try:
        return json.loads(resposta_str)
    except json.JSONDecodeError:
        raise ValueError("Resposta do modelo não está em formato JSON válido.")


CATEGORIAS_PERMITIDAS = [
    "elogio",
    "reclamação",
    "dúvida",
    "cancelamento"
]

def validar_categoria(categoria):
    if categoria not in CATEGORIAS_PERMITIDAS:
        raise ValueError(f"Categoria inválida: {categoria}")
