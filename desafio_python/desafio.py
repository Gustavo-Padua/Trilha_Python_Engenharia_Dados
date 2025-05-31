menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def saque(valor_saque):
    global extrato
    global numero_saques
    global limite
    global saldo

    if valor_saque:
        if saldo >= valor_saque:
            if valor_saque <= limite:
                if numero_saques < LIMITE_SAQUES:
                    saldo -= valor_saque
                    numero_saques += 1
                    print("Saque realizado com sucesso!\n")
                    extrato += f"Valor do Saque: {valor_saque:.2f}\n"
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


def deposito(valor_deposito):
    global saldo
    global extrato
    if valor_deposito:
        saldo += valor_deposito
        print("Depósito realizado com sucesso!")
        extrato += f"Valor do depósito: {valor_deposito:.2f}\n"
    else:
        print("Valor inválido para depósito")


def extrato_conta():
    global extrato
    print("\n=============== Extrato ==============\n")
    if not saldo:
        if not extrato:
            print("Não foram realizadas movimentações!")
    else:
        print(extrato)

    print(f"O saldo atual da conta é: R${saldo}\n")  
    print("======================================\n")


while True:

    opcao = input(menu)

    try:
        if opcao == "d":
            valor_deposito = int(input("Informe o valor a ser depositado: R$"))
            deposito(valor_deposito)

        elif opcao == "s":
            valor_saque = int(input("Informe o valor a ser sacado: R$"))
            saque(valor_saque)

        elif opcao == "e":
            extrato_conta()
                
        elif opcao == "q":
            break
    
    except ValueError:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


