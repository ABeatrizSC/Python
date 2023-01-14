#69
#Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou nao continuar. No final, mostre:
#a) quantas pessoas tem mais de 18 anos
#b) quantos homens foram cadastrados
#c) quantas mulheres tem menos de 20 anos

cont_idade = 0
cont_homem = 0
cont_mul = 0
while True:
    print("CADASTRO DE PESSOAS", " ")
    idade = int(input("Idade: "))
    sexo = str(input("Qual o sexo? [F/M]"))
    if idade > 18:
        cont_idade += 1
    if sexo == 'm' or sexo == 'M':
        cont_homem += 1
    if sexo == 'f' or sexo == 'F':
        if idade < 20
            cont_mul += 1
    resp = str(input("Quer cadastras mais? [s/n]"))
    if resp == 'n' or resp == 'N':
        break

print(f"Há {cont_idade} pessoas maiores de 18 anos.")
print(f"Há {cont_homem} homens cadastrados.")
print(f"Há {cont_mul} mulheres com menos de 20 anos cadastradas.")