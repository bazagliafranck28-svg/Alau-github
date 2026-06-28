def formatar_real(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Exemplo de uso
preco_hospedagem = float(input("Digite o valor da hospedagem: "))
print(formatar_real(preco_hospedagem))  # R$ 49,90

