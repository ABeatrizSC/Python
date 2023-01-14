#68
#Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias ele conquistou no final do jogo.

import random
from random import randint
resp = str("s")
while resp == 's' or resp == 'S':
    while True:
        vit_pc = 0
        vit_jogador = 0
        print('=-' * 20)
        print("    VAMOS JOGAR PAR OU ÍMPAR? ")
        print('=-' * 20)
        numero = int(input("Digite o número: "))
        par_impar = str(input("Par ou ímpar? [P/I]"))
        numero_pc = random.randint(0, 10)
        print(" ")
        print("=-"*20)
        print(f"Você jogou o numero {numero} e máquina {numero_pc}")
        print('=-' * 20)
        if (numero + numero_pc)%2==0:
            print("A soma dos dois números apostados foi PAR!")
            if par_impar == 'P' or par_impar == 'p':
                print('=-' * 20)
                print("JOGADOR GANHOU!")
                print(" ")
                print(" ")
                vit_jogador += 1
            else:
                print('=-' * 20)
                print("MÁQUINA GANHOU!")
                print("=-"*20)
                print(" ")
                print(" ")
                vit_pc += 1
        else:
            print("A soma dos dois números apostados foi IMPAR!")
            if par_impar == 'I' or par_impar == 'i':
                print('=-' * 20)
                print("  JOGADOR GANHOU!")
                print(" ")
                print(" ")
                vit_jogador += 1
            else:
                print('=-' * 20)
                print("  MÁQUINA GANHOU!")
                print("=-"*20)
                print(" ")
                print(" ")
                vit_pc += 1
        if vit_pc != 0:
            break
print('=-'*10)
print("  VOCÊ PERDEU! ")
print('=-'*10)
print(f"Vitórias acumuladas: {vit_jogador}")
print('=-'*10)
resp = str(input("Quer jogar novamente? [s/n]"))
     