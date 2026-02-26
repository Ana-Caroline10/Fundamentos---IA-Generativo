from classifier import classificar_mensagem

mensagens_cliente = [
    "Quero contratar o plano premium",
    "O sistema está com erro",
    "Quero cancelar minha assinatura",
    "Quero falar com um atendente",
    "Preciso de ajuda com meu pagamento",
    "Gostaria de atualizar minhas informações de conta",
    "Vocês trabalham no sábado"
]

temperaturas = [0.0, 0.5, 1.0]

total_execucoes = 0
total_erros = 0

for rodada in range(1, 11):
    print(f"\n================ RODADA {rodada} ================\n")

    for temp in temperaturas:
        print(f"\n---- Temperatura: {temp} ----\n")

        for mensagem in mensagens_cliente:
            print(f"Cliente: {mensagem}")
            total_execucoes += 1

            try:
                resposta = classificar_mensagem(mensagem, temperature=temp)
                print(f"Resposta: {resposta}\n")

            except Exception as e:
                total_erros += 1
                print(f"Erro ao processar mensagem: {e}\n")

print("\n================ RESULTADO FINAL ================\n")
print(f"Total de execuções: {total_execucoes}")
print(f"Total de erros: {total_erros}")

if total_execucoes > 0:
    taxa_erro = (total_erros / total_execucoes) * 100
    print(f"Taxa de erro: {taxa_erro:.2f}%")
