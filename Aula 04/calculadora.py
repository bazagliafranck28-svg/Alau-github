# CALCULADORA BÁSICA
print("=== Calculadora ===\n")

num1 = float(input("Digite o primeiro numero: "))
operador = input("Digite o operador (+, -, /, *)")
num2 = float(input("Digite o segundo numero: "))

if operador == "+":
     print(num1+num2)
elif operador == "-":
     print(num1-num2)
elif operador == "/":
     if num2 == 0:
          print(" Erro divisão por zero")
     else:
          print(num1/num2)
elif operador == "*":
     print(num1*num2)
else:
     print("operdor inexistente")
