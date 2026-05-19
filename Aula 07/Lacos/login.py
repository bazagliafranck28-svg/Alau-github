login = input("Login: ")
senha = input("Senha: ")

while True: 
    if login == "Franck" and senha == "1234" : # if = comparar
        print("Acesso realizado com sucesso")
        break
    else: # caso contrario
        print("Tente novamente!")