def estatisticas(*numeros):
    total = sum(numeros)    
    media = total / len(numeros)
    maximo = max(numeros)   
    minimo = min(numeros)
    print(f"total: {total} | média: {media:.2f} | máximo: {maximo:.2f} | mínimo: {minimo}")

estatisticas(59, 60, 80, 90, 46)
estatisticas(70, 89, 49)
#listas
listas = [80,90,95]
estatisticas(*listas)  #desempacotando a lista
 
    