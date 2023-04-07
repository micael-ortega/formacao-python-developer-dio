"""OBJETIVO GERAL:
Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato


-OPERAÇÃO DE DEPÓSITO:
Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

-OPERAÇÃO DE SAQUE:
O sistema deve permitir realizar 3 saques diários com limite máximo de R$500 por saque
Caso o usuário não tenha saldo o sistema deve exibir uma mensagem informando que não será 
possível sacar por falta de saldo.
Toda as operações de saque devem ser exibidas na operação de extrato.

-OPERAÇÂO EXTRATO:
Esta operação deve listar todos os depósitos e saques realizados  na conta.
No final deve ser exibido o saldo atual da conta.
Se o extrato estiver em branco, exibir a mensagem "Não foram realizadas movimentações."
Os valores devem ser exibidos no formato R$ XXX.xxx
"""

menu = """
[d] = Depósito
[s] = Saque
[e] = Extrato
[q] = Sair

=>"""

saldo = 0
extrato = ""
saque_count = 0
SAQUE_LIMITE = 500

while True:
    opcao = str(input(menu))
    # Operação de depósito
    if opcao == "d":

        # Armazena o valor depósito na variável deposito
        deposito = float(input("Valor do depósito: "))

        if deposito <= 0:
            print("Insira um valor válido para depósito")
        else:
            # Incrementa o valor do saldo com o depósito
            saldo += deposito
            # Adiciona a string extrato o valor do depósito
            extrato += f"Depósito: + R${deposito:.2f}\n"

    # Operação de saque
    elif opcao == "s":
        # Armazena o valor de saque na variavel saque
        saque = float(input("Valor do saque: "))
        # Criadas as regras de saque nas condicionais para saldo_insuficiente, saques_diarios e limite_saque
        saldo_insuficiente = saldo <= 0
        saques_diarios = saque_count >= 3
        limite_saque = saque > SAQUE_LIMITE
        if saldo_insuficiente:
            print("Saldo insuficiente para saque")
        elif saques_diarios:
            print("Quantidades de saques diários excedida")
        elif limite_saque:
            print("Valor limite de saque excedido")
        else:
            # O contador de saques incrementa a cada saque realizado
            saque_count += 1
            # Decrementa do saldo o valor do saque
            saldo -= saque
            # Adiciona a string extrato a operação de saque realizada
            extrato += f"Saque:    - R${saque:.2f}\n"

    elif opcao == "e":
        print("====================EXTRATO====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo:      R${saldo:.2f}")
        print("===============================================")
    elif opcao == "q":
        break

    else:
        print("Opção inválida.")
