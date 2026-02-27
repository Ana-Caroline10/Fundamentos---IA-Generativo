import json

def validate_json(response_text):
    try:
        data = json.loads(response_text)

        if "status" not in data:
            return False, "Campo 'status' obrigatório"

        if "resposta" not in data:
            return False, "Campo 'resposta' obrigatório"

        return True, data

    except json.JSONDecodeError as e:
        return False, f"Erro ao decodificar JSON: {e}"
