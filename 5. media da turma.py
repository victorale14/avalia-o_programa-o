n = int(input("Digite o número de alunos: "))

notas = []

for _ in range(n):
    nota = float(input())
    notas.append(nota)  # Aqui adicionamos a nota na lista

soma = 0
for nota in notas:
    soma += nota

media = soma / n

acima_10_porcento = 0
abaixo_10_porcento = 0

for nota in notas:
    if nota > media * 1.1:
        acima_10_porcento += 1
    elif nota < media * 0.9:
        abaixo_10_porcento += 1

print(f"{media:.2f}")
print(acima_10_porcento)
print(abaixo_10_porcento)