#87
#Aprimorando o exercício anterior, faça: 
#1- a soma de todos os valores pares digitados
#2- a soma de todos os valores da terceira coluna
#3- o maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
totpar = 0
somaterc = 0


for l in range (0, 3):
  for c in range (0, 3):
    matriz[l][c] = int (input(f"Digite o valor da posição [{l},{c}]: "))
    if matriz[l][c]%2==0:
      totpar += matriz[l][c]
 
for l in range (0, 3):
  somaterc += matriz[l][2]

maiorv = matriz[1][0]
for c in range (0, 3):
  if matriz [1][c] > maiorv:
    maiorv = matriz [1][c]
  

print ('-=' * 30 )
for l in range (0, 3):
  for c in range (0, 3):
    print(f"[{matriz[l][c]}]", end="")
  print()  

print (f"A soma dos numeros da terceira coluna é: {somaterc}")  
print (f"A soma dos numeros da pares digitados é: {totpar}")
print (f"O maior numero da segunda linha é: {maiorv}")