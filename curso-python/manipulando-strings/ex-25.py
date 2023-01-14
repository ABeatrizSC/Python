#25
#Crie um programa que leia o nome de uma pessoa e diga se ela tem “Silva” no nome.

nome = str(input("Digite seu nome: "))
nome = nome.title() 
if 'Silva' in nome:
    print("Você tem Silva no nome.")
else:
    print("Você não tem Silva no nome.")