numero = int(input("Digite um número: "))

if numero < 2:
    print("Número não é Primo")
else:
    primo = True
    for i in range(2, numero):  
        if numero % i == 0:
            primo = False
            break 
    if primo:
        print("Número Primo")
    else:
        print("Número não Primo")
        