#78
#Faça um programa que leia 5 valores e guarde-os em uma lista. No fim ,mostre qual o maior e o menor valor digitado, e as suas respectivas posições na lista.

valores = []

for v in range(0,5):
  valores.append(int(input(f"Digite o valor {v}:")))

maior = valores[0]
menor = valores[0]

for v in range (0,5):
  if valores[v] > maior:
    maior = valores[v]
  if valores[v] < menor:
    menor = valores[v]  

for c, v in enumerate (valores):
  if v == maior:
    posicaomaior = c
  if v == menor:
    posicaomenor = c   

print (f"O maior numero digitado foi {maior} na posição {posicaomaior}")  
print (f"O menor numero digitado foi {menor} na posição {posicaomenor}")  
     