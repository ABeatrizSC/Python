#80
#Crie um programa onde o usuario digite 5 numeros e coloque-os em ordem crescente sem utilizar o sort().

numeros = []

for i in range (0,4):
  n = int (input(f"Digite o numero da posição {i}:"))
  if i == 0: 
    numeros.append(n) 
  elif n > numeros[-1]: 
    numeros.append(n) 
  else:
    posicao = 0
    while posicao < len(numeros): 
      if n <= numeros[posicao]: 
          numeros.insert(posicao,n) 
          break 
    posicao += 1  

print (f"os valores digitados em ordem foram: {numeros}")