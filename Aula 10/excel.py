def se(condicao, valor_se_verdadeiro, valor_se_falso):

    return valor_se_verdadeiro if condicao else valor_se_falso

alunos = [
    ("João", 40),
    ("Maria", 60),
    ("josé", 94),
    ("Pedro", 70),
    ("Ricardo", 91),
    ("Bruna", 56),
    ("Silas", 51),
    ("Patricia", 36),
    ("Tatiana", 82),
    ("Roseane", 36),
    ("Carlos", 65),
    ("Marcos", 73),
    ("Adrana", 91),
    ("adriano", 32),
    ("Franck", 95),
    ]
print(f"{'Aluno': ^15} {'Nota': ^6} {'Situação': ^12}")
print("-" * 38)

for nome, nota in alunos:
    situacao = se(nota >= 70, "Aprovado", se(nota >= 50, "Recuperação", "Reprovado"))
    
    print(f"{nome:15} {nota:>6} {situacao:^12}")

print("-" * 38)

print("\n --- boletim ---")

aprovados = 0
reprovados = 0
recuperacao = 0

for nome, nota in alunos:
    situacao = se(nota >= 70, "Aprovado", se(nota >= 50, "Recuperação", "Reprovado"))

    if situacao == "Aprovado":
        aprovados += 1
    elif situacao == "Reprovado":
        reprovados += 1
    else:
        recuperacao += 1

#Exibe o resultado
print(f"Total de aprovados: {aprovados}")
print(f"Total de reprovados: {reprovados}") 
print(f"Total de alunos em recuperação: {recuperacao}") 
