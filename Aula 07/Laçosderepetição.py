procure = input("Pesquisar peça:")
estoque = ["prego", "Pocar", "Arruela", "Parafuso","Mola"]
for item in estoque:
    if item == procure:
        print("Item encontrado no estoque!")
        break #Interrope o laço imediatamente
else:
    print("Item não encontrado após varredura completa.")
