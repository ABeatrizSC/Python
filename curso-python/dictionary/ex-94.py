#94
#Crie um programa que leia nome, sexo e idade de várias pessoas, mandando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final mostre:
#a) quantas pessoas foram cadastradas.
#b) a média de idade do grupo.
#c) uma lista com todas as mulheres.
#d) uma lista com todas as pessoas com idade acima da média.

dados = {}
lista = []
mulher_list = []
tot = 0
media = float(0)
tod_idades = 0
acimamed_list = []
print("CADASTRO")
while True:
    dados['nome'] = str(input("Nome: "))
    dados['sexo'] = str(input("Sexo [F/M]: "))
    dados['idade'] = int(input("Idade: "))
    tot += 1
    lista.append(dados.copy())
    if dados['sexo'] in 'Ff':
        mulher_list.append(dados.copy())
    dados.clear()
    resp = str(input("Deseja cadastrar mais? [s/n]: "))
    if resp in 'Nn':
        break

for i in range (len(lista)):
    tod_idades += lista[i]['idade']

media = tod_idades/tot

if lista[i]['idade'] > media:
    acimamed_list.append(lista[i])

print(f"Lista com todas as mulheres cadastradas: {mulher_list}")
print(f"A média de idade das pessoas cadastradas: {media}")
print(f"Pessoas acima da média de idade: {acimamed_list}")
print(f"Total de pessoas cadastradas: {tot}")