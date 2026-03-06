import datetime
import random
import string


def data_atual():
    return str(datetime.date.today())


def calcular_idade(ano_nascimento):
    ano_atual = datetime.date.today().year
    return ano_atual - int(ano_nascimento)


def gerar_senha(tamanho=10):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(int(tamanho)))
    return senha
