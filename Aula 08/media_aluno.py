# Entrada das notas
n1 = float(input("Nota1: "))
n2 = float(input("Nota2: "))
n3 = float(input("Nota3: "))
n4 = float(input("Nota4: "))

soma = n1 + n2 + n3 + n4
media = soma / 4

if media >= 7.0:
    resultado = "Aprovado"

elif media >= 5.0:
    resultado = "Recuperação"

else:
    resultado = "Reprovado"

print("Nota 1:", n1)
print("Nota 2:", n2)
print("Nota 3:", n3)
print("Nota 4:", n4)
print("Média:", media)
print("Resultado:", resultado)

