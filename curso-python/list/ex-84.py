#84
#faça um programa que leia nome e peso, e guarde-os em uma lista.
#depois, exiba quantas pessoas foram cadastradas, junto com um listagem de pessoas mais pesadas e menos pesadas

dados = []
auxiliar = []
maior = menor = 0


while True:
  auxiliar.append(input("Nome:"))
  auxiliar.append(input("Peso:"))
  if len(dados) == 0: 
    maior = menor = auxiliar [1] 
  else:
    if auxiliar[1] > maior:
      maior = auxiliar[1] 
    if auxiliar[1] < menor:
      menor = auxiliar[1]     
  dados.append(auxiliar[:])
  auxiliar.clear()
  resposta = str(input("Quer continuar [s/n]"))
  if resposta in 'Nn':
    break 


print ("-"*30) 
print(f"O numero de pessoa cadastradas foi: {len(dados)}") 
print(f"O maior peso foi de {maior} kg. Peso de ", end= '')
for p in dados:
    if p[1] == maior:
        print (f"{p[1]}", end='')
print ()     
print(f"O menor peso foi de {menor} kg. Peso de ", end= '')
for p in dados:
    if p[1] == menor:
        print (f"{p[1]}", end='') 
print ()  