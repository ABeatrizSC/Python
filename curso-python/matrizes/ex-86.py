#86 - MATRIZES
#Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado. No final, exiba a matriz com a formação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #cada linha com três valores vazios (0) p nao precisar usar append!

for l in range (0, 3):
  for c in range (0, 3):
    matriz[l][c] = int(input(f"Digite o valor para: [{l}, {c}]"))

print ('-=' * 30 )
for l in range (0, 3):
  for c in range (0, 3):
    print(f"[{matriz[l][c]}]", end="")
  print()  