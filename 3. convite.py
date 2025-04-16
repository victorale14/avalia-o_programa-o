nome = input("Ola! qual seu nome? ")
if len(nome) >= 120:
    print("Digite um nome com menos de 120 caracteres!")  
    exit()

print(f"seja bem vindo(a), {nome}!")