# **kwargs - argumentos nomeados variaveis
#captura qualquer qauntidade de argumentos nomeados e os armazena em um dicionário


def exibir_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")  

exibir_info(nome="João", idade=30, cidade="São Paulo")
partido="bolsomaro"
