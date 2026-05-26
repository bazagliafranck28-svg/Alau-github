saldo = 0.0

print("Bem-vindo ao banco Sicredi!")
while True:
    print("\nEscolha uma opção:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")

    op = input("Escolha: ")
    if op == "1":
        valor = float(input("Valor para depositar: R$ "))
        saldo += valor
        print(f"Depositado! Saldo atual: {saldo:.2f}")
    elif op == "2":
        valor = float(input("Valor para sacar: R$ "))
        if valor <= saldo:
            saldo -= valor
            print(f"Saque realizado com sucesso! saldo atual: R${saldo:.2f}")
        else:
            print("Saldo insuficiente")
    elif op == "3":
        print(f"Seu saldo é: R${saldo:.2f}")
    elif op == "4":
        print("Obrigado por usar o banco Sicredi!")
        break
    else:
        print("Opção inválida. Tente novamente.")
        