
#70
#Crie um programa que leia o nome e preço de varios produtos. O programa deverá perguntar se o usuário vai continuar e no final mostre:
#a) qual é o total gasto na compra
#b) quantos produtos custam mais de 1.000
#c) qual o nome do produto mais barato

print("-="*15)
print("       COMPRAS DO MÊS  ")
print("-="*15)

tot = 0
maisdemil = 0
cont = 0
while True:
    prod = str(input("Nome do produto: "))
    preco = float(input("Preço: "))
    if cont == 0:
        maisbarato = preco
        nome_maisbarato = prod
        cont +=1
    tot += preco
    if preco > 1000:
        maisdemil += 1

    if preco < maisbarato:
        maisbarato = preco
        nome_maisbarato = prod
    resp = str(input("Deseja continuar? [S/N]"))
    if resp == 'N' or resp == 'n':
        break
    else:
        continue

print(f"Total de gastos na compra R${tot}")
print(f"Produtos que custam mais de mil reais: {maisdemil}")
print(f"O produto mais barato é {nome_maisbarato} que custa R${maisbarato}")