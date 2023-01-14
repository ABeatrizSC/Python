#23
#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex: Digite um número: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

numero = str(input("Digite um numero: "))
if len(numero) > 4:
    print("Numero invalido. Digite novamente.")
    numero = str(input("Digite um numero: "))
else:
    if len(numero) == 1:
        print("Unidade: {}".format(numero[0]))
    elif len(numero) == 2:
        print("Unidade: {}".format(numero[1]))
        print("Dezena: {}".format(numero[0]))

    elif len(numero) == 3:
        print("Unidade: {}".format(numero[2]))
        print("Dezena: {}".format(numero[1]))
        print("Centena: {}".format(numero[0]))

    elif len(numero) == 4:
        print("Unidade: {}".format(numero[3]))
        print("Dezena: {}".format(numero[2]))
        print("Centena: {}".format(numero[1]))
        print("Milhar: {}".format(numero[0]))