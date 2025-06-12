
def menu():
    menu = input("""

    [c]  Cadastrar Cliente
    [cc] Criar Conta
    [lc] Listar Conta
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [q]  Sair

    => """)

    return menu


def cadastro_cliente(lista_clientes):
    cpf = input("Informe seu CPF (Apenas números): ")
    cliente = filtrar_cliente(cpf, lista_clientes)

    if cliente:
        print("Já existe ususário com esse CPF!")
        return        
    else:
        print("""
        Por favor, preencher as seguintes informações para cadastro do cliente: \n
        """)
                
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento (dd-mm-aaaa): ")
        endereco = input("Endereço (logradouro, nº - bairro - cidade/sigla estado): ") 

        lista_clientes.append({"nome": nome, "data de nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})            

    print("Cliente cadastrado com sucesso!")


def filtrar_cliente(cpf, lista_clientes):
    clientes_filtrados = [cliente for cliente in lista_clientes if cliente["cpf"] == cpf ]
    return clientes_filtrados[0] if clientes_filtrados else None


def criar_conta(agencia, numero_conta, lista_clientes):
    cpf = input("Informe seu CPF (Apenas números): ")
    cliente = filtrar_cliente(cpf, lista_clientes)

    if cliente:
        print("\nConta criada com sucesso!")
        return {"agência": agencia, "número da conta": numero_conta, "cliente": cliente}
    else:
        print("Cliente não cadastrado! Necessário ter cadastro para criação de conta!")


def consultar_conta(lista_contas):
    for conta in lista_contas:
        linha = f"""\
            Agência:\t{conta['agência']}
            C/C:\t{conta['número da conta']}
            Titular:\t{conta['cliente']['nome']}
        """
        print("=" * 100)
        print(linha)


def saque(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):

    if valor_saque:
        if saldo >= valor_saque:
            if valor_saque <= limite:
                if numero_saques < limite_saques:
                    saldo -= valor_saque
                    numero_saques += 1
                    print("Saque realizado com sucesso!\n")
                    extrato += f"Valor do Saque: R$ {valor_saque:.2f}\n"
                    print(f"Seu saldo atual é de: R$ {saldo:.2f}\n")
                else:
                    print("Limite de saque excedido!")
        
            else:
                print("Valor de saque informado maior que o limite permitido!\n")
                print("Limite de saque: R$500,00\n")
                print("Tente novamente!\n")
             
        else:
            print("Saldo insuficiente para efetuar o saque do valor informado!")
    else:
        print("Valor informado inválido para saque!")      

    return saldo, extrato


def deposito(saldo, valor_deposito, extrato, /):

    if valor_deposito:
        saldo += valor_deposito
        print("Depósito realizado com sucesso!")
        extrato += f"Valor do depósito: R$ {valor_deposito:.2f}\n"
        print(extrato)
        print(f"Seu saldo atual é de: R$ {saldo:.2f}\n")
    else:
        print("Valor inválido para depósito") 

    return saldo, extrato


def extrato_conta(saldo,/,*,extrato):

    print("\n=============== Extrato ==============\n")
    if not saldo:
        if not extrato:
            print("Não foram realizadas movimentações!")
    else:
        print(extrato)

    print(f"O saldo atual da conta é: R${saldo}\n")  
    print("======================================\n")


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    lista_clientes = []
    lista_contas = []

    while True:

        opcao = menu()

        try:
            if opcao == "c":
                cadastro_cliente(lista_clientes)                

            elif opcao == "cc":
                numero_conta = len(lista_contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, lista_clientes)

                if conta:
                    lista_contas.append(conta)

            elif opcao == "lc":
                consultar_conta(lista_contas)

            elif opcao == "d":
                valor_deposito = int(input("Informe o valor a ser depositado: R$"))

                saldo, extrato = deposito(saldo, valor_deposito, extrato)

            elif opcao == "s":
                valor_saque = int(input("Informe o valor a ser sacado: R$"))
                
                saldo, extrato = saque(saldo=saldo, valor_saque=valor_saque, extrato=extrato, limite=limite, 
                      numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

            elif opcao == "e":
                extrato_conta(saldo, extrato=extrato)
                
            elif opcao == "q":
                break
    
        except ValueError:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

    return False


main()