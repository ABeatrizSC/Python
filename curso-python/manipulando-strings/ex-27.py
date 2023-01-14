#27
#Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e último nome separadamente.
#Ex: Ana Maria de Souza
#primeiro: Ana
#último: Souza

nome = str(input("Digite seu nome completo: "))
nomesep = nome.split()
print("Primeiro: {}".format(nomesep[0]))
ultimo = len(nomesep)
print("Ultimo: {}".format(nomesep[ultimo-1]))