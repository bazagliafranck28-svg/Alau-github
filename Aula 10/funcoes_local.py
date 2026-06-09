nome = "Python" #Global 
def mostrar_nome():
    nome = "javascript" #Local
    print(nome) #javascript

mostrar_nome()
print(nome) #Python
