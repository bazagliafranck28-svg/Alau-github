procurar = input("Pesquisar peça: ")
estoque = ["Prego","Porca","Arruela","Parfuso","Mola"
"Parufo","Mola"]

for item in estoque: 
    if item == procurar:
     print("item encontrado no estoque!")
     break
else:
    print("Item não encontrado")