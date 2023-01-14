#24
#Crie um programa que diga se o nome de uma pessoa começa ou não com nome “Santos”.

nome = str(input("Digite seu nome: ")).strip() 
nome = nome.title() 
separa = nome.split()
if separa[0] == 'Santos':
    print("Seu nome começa com Santos.")
else:
    print("Seu nome não começa com Santos.")
