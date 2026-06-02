import random 
simbolos = ["🐂","🐻","❤️","🦖","🌛","😡"]
saldo = 20
print("=== Kassinão do Senai ===\n")
while saldo >= 2:
    input ("\npressione ENTER para girar (custa R$ 2,00)...")
    saldo -= 2

    resultado = [random.choice(simbolos) for _ in range(3)]
    print(" |".join(resultado))

    if resultado[0] == resultado[1] == resultado[2]:
        premio = 20
        saldo += premio
        print(f"  JACKPOT!!! Voce ganhou R$ {premio}!")

    elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
        premio = 5
        saldo += premio

        print(f"  Parabéns! Voce ganhou R$ {premio}!")
    else:
        print("Não foi dessa vez...")

        print(f"Saldo atual: R$ {saldo:.2f}")
        




