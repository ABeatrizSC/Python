#66
#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No fnal, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsideando o flag)

tot_num = 0
soma = 0
while True:
  numero = int(input("Digite um numero: "))
  if numero != 999:
    tot_num += 1
    soma += soma + numero
  else:
   break   
print(f"Total de numeros digitados: {tot_num}") 
print(f"Soma dos numeros digitados: {soma}")