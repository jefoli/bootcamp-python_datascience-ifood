LIMITE_SAQUES = 3
MSG_ADVICE = f"Consulte seu gerente para mais informações.\n"
saldo = 0
limite = 500
numero_saque = 0
extrato = ""

import datetime
current_date = datetime.datetime.now().isoformat(sep=" ", timespec="seconds")

def deposito(valor_dep):
    global extrato, saldo
    if valor_dep <= 0:
        print("Valor inválido. Tente novamente!\n")
    else:
        saldo += saldo+ valor_dep
        print("Depósito realizado com sucesso!\n")
        print(saldo)
        extrato += f"{current_date} R$ + {valor_dep:.2f}\n"
    return saldo

def saque(numero_saque):
    global extrato, saldo
    if numero_saque > 2:
        print(f"\nLimite de operações excedidas para este tipo de conta!\nQuantidade de saques disponíveis para essa conta: {LIMITE_SAQUES} (três).")
        print(MSG_ADVICE)
    elif valor_saq <= 0:
        print("Valor inválido!")
    elif valor_saq > limite:
        print(f"\nO valor informado excede o o limite disponível para essa conta.\nLimite de valor por saque R$: {limite:.2f}!")
        print(MSG_ADVICE)
    elif valor_saq > saldo:
        print("Você não possui saldo suficiente para esta operação!\n")
    else:
        saldo = saldo - valor_saq
        numero_saque += 1
        extrato += f"{current_date} R$ -{valor_saq:.2f}\n"
        print(f"Operação realizada com sucesso!\n")
    return numero_saque

#fun extrato
def extratos():
    print("Não foram realizadas movimentações. ") if extrato == "" else print(f"Extrato consolidado:\n\n{extrato}"), print(f"Saldo total R$: {saldo:.2f}")
    return

print("Bem-vindo ao BTG Pactual!\n")

menu = """Escolha uma das opções abaixo:\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\n=> """

while True:
    opcao = input(menu)
    if opcao == "d":
        valor_dep = int(input("Informe o valor que deseja depositar R$: "))
        deposito(valor_dep)
    elif opcao == "s":
        valor_saq = int(input("Informe o valor que deseja sacar R$: "))
        saque(valor_saq)
    elif opcao == "e":
        extratos()    
    elif opcao == "q":
        print("O banco BTG agradece a sua parceria!\nVolte sempre!")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.\n")


