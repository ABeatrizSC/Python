#82
#Crie um programa que leia vários numeros e o coloque em uma lista, depois crie duas listas extras, uma só com números ímpares, outra só com números pares. Exiba as três.

numeros = []
pares = []
impares = []

resposta = "s"
while resposta == "s":
  numeros.append(int(input(f"Digite o numero:")))
  resposta = (input("Quer continuar? [s/n]"))
  if resposta == "n":
    break

for i in range (len(numeros)):
  if numeros[i]%2==0:
    pares.append(numeros[i])
  else:
    impares.append(numeros[i])

print(f"lista completa {numeros}")
print(f"lista só com pares {pares}")
print (f"lista só com impares {impares}") 