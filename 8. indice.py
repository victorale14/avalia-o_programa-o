texto = input()
caractere = input()

indice = -1

for i in range(len(texto)):
    if texto[i] == caractere:
        indice = i
        break

print(indice)
