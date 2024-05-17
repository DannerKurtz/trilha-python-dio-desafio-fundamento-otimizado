import textwrap


def menu():
    lista_menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Conta
    [nu] Novo Usuário
    [q] Sair

 """
    print(lista_menu)
    return input("=> ")

def deposito(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("VALOR DEPOSITADO COM SUCESSO!")
    else:
        print("Operação inválida")
    return saldo, extrato

def sacar(valor, saldo, limite, numero_saques, LIMITE_SAQUES, extrato):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF: ")
    usuarios_filtrados = filtrar_usuarios(cpf, usuarios)

    if usuarios_filtrados:
        print("Usuario já existente")
        return  

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço completo: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})


def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu CPF: ")
    filtrar_usuarios(cpf, usuarios)

    if usuarios:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuarios}
    print("Usuario não encontrado")

def listar_contas(contas):
    for conta in contas:
        # Verificar se 'usuario' é uma lista e acessar o primeiro elemento se for o caso
        if isinstance(conta['usuario'], list) and conta['usuario']:
            usuario = conta['usuario'][0]
        else:
            usuario = conta['usuario']

        linha = textwrap.dedent(f"""
            Agência:    {conta['agencia']}
            C/C:        {conta['numero_conta']}
            Titular:    {usuario['nome']}
        """)
        print(linha)

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    while True:

        
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            
            saldo, extrato = deposito(valor, saldo, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(valor, saldo, limite, numero_saques, LIMITE_SAQUES, extrato)
            

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            break

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
