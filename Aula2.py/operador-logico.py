idade = int(input("Digite sua idade: "))

cnh = input("Tem CNH? (SIM/NÃO): ")
if idade >= 18 and cnh == "sim" :
    print("Pode dirigir")
else:
    print("Não pode dirigir")
   

    