
n = int(input("Quantos números você vai digitar? "))

numeros = []

for _ in range(n):
    numero = int(input())
    numeros.append(numero)

print("a) Ordem inversa:")
for num in reversed(numeros):
    print(num)

print("b) Ordem decrescente:")
for num in sorted(numeros, reverse=True):
    print(num)
