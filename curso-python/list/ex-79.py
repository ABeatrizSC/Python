#79
#Crie um programa onde o usuário possa digitar diversos valores numéricos e cadastre-os em uma lista. Caso o numero já exista la dentro, ele não será adicionado. No final, serão exibidos todos os valores unicos digitados, em ordem crescente.

valores = []
x = int (input("Digite o numero de valores que deseja cadastrar: "))

for v in range (0,x):
      num = int(input(f"Digite o valor da posição {v}: "))
      if num not in valores:
        valores.append(num)        
valores.sort()
print (f'números digitados: {valores}')
     