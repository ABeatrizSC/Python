#81
#Crie um programa que leia vários números em uma lista e depois disso, mostre: quantos numeros foram digitados, a lista ordenada de forma decrescente e se o valor 5 está ou nao na lista.

lista = []
resposta = "s"
while resposta == "s":
  lista.append(int(input("Digite um valor:")))
  resposta = (input("Quer adicionar mais valores? [s/n]"))
  if resposta == "n":
        break
  else:
    resposta = "s"      
cont = 0
for i in lista:
  cont += 1 

print (f"O total de numeros digitados foi {cont} numeros") 

if 5 in lista:
  print ("Há o numero 5 entre os valores digitados")
else:
  print ("não há valores 5 digitados.")

lista.reverse()
print (f"lista digitada em ordem decrescente: {lista}")  