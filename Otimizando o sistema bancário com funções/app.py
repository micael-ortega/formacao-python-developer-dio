"""OBJETIVO GERAL:
Separar as funções existentes de saque, depósito e extrato em funções 
Criar duas novas funções: criar usuário, e criar conta corrente
OBS: implementar listar contas

A função SAQUE deve receber argumentos apenas por nome 
Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques
Sugestão de retorno: saldo e extrato

A função DEPOSITO deve receber argumentos apenas por posição
Sugestão de argumentos: saldo, valor, extrato
Sugestão de retorno saldo e extrato

A função EXTRATO deve receber argumentos por posição e nome
Argumentos posicionais: saldo
Argumento nomeado: extrato

A função CRIAR USUARIO deve armazenar os usuarios em uma lista
um usuário é composto por nome, data de nascimento, cpf e endereço
O endereço é uma string com formato: logradouro - nro - cidade/UF
deve ser armazenado somente os numeros do CPF. 
Não podemos cadastrar 2 usuários com o mesmo CPF

A função CRIAR CONTA CORRENTE deve armazenar contas em uma lista
uma conta é composta por agência, numero da conta e usuario
O numero da conta é sequencial, iniciando em 1
O numero da agencia é fixo 0001
O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário

DICA 
para vincular um usuário a uma conta filtre a lista de usuários 
buscando o numero do cpf informado para cada usuario da lista
Se eu não encontrar uma conta de usuário não é possivel criar uma conta
"""


def depositar(saldo, valor, extrato, /):
    # Armazena o valor depósito na variável deposito
    if valor <= 0:
        print("Insira um valor válido para depósito")
    else:
        # Incrementa o valor do saldo com o depósito
        saldo += valor
        # Adiciona a string extrato o valor do depósito
        extrato += f"Depósito:\t\tR${valor:.2f}\n"

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # Criadas as regras de saque nas condicionais para saldo_insuficiente, saques_diarios e limite_saque
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("Saldo insuficiente para saque")
    elif excedeu_limite:
        print("Valor limite de saque excedido")
    elif excedeu_saques:
        print("Quantidades de saques diários excedida")
    elif valor > 0:
        # O contador de saques incrementa a cada saque realizado
        numero_saques += 1
        # Decrementa do saldo o valor do saque
        saldo -= valor
        # Adiciona a string extrato a operação de saque realizada
        extrato += f"Saque:\t\t\tR${valor:.2f}\n"
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido")

    return saldo, extrato


def imprime_extrato(saldo, /, *, extrato):
    print("===============================================")
    print("====================EXTRATO====================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo:\t\t\t${saldo:.2f}")
    print("===============================================")



def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuarios(cpf, usuarios)
    # Se usuário já é encontrado retorna a função principal
    if usuario:
        print("Usuário já cadastrado com este CPF!")
        return
    # Entra com dados para cadastro do usuário
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    logradouro = input("Informe o logradouro: ")
    nro = input("Informe o número: ")
    cidade = input("Informe a cidade: ")
    uf = input("Informe a UF: ")
    endereço = f"Logradouro: {logradouro}, Número: {nro}, Cidade/UF: {cidade}/{uf}"
    cpf = str(cpf).replace(".", "").replace("-", "")
    usuario = {
        "cpf": cpf,
        "nome": nome,
        "data de nascimento": data_nascimento,
        "endereço": endereço
    }
    # Adiciona usuário cadastrado a lista usuários
    return usuarios.append(usuario)


def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")

        return {"agencia": agencia, "numero da conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado, fluxo de criação de conta encerrado")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero da conta']}
            Usuário:\t{conta['usuario']['nome']}
        """
        print("="*50)
        print(linha)


def menu():
    menu = """
    [d] = Depósito
    [s] = Saque
    [e] = Extrato
    [u] = Cadastrar Usuário
    [c] = Cadastrar Conta Corrente
    [l] = Listar contas
    [q] = Sair

    =>"""
    return input(menu)


def main():

    saldo = 0
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    limite = 500
    usuarios = []
    AGENCIA = "0001"
    numero_conta_corrente = 0
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = int(input("Valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques)
        elif opcao == "e":
            imprime_extrato(saldo, extrato=extrato)
        elif opcao == "u":
            criar_usuario(usuarios)
        elif opcao == "c":
            numero_conta_corrente += 1
            conta = criar_conta(AGENCIA, numero_conta_corrente, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "l":
            listar_contas(contas)
        elif opcao == "q":
            break


main()
