#71
#Crie um programa que simule o funcionamento de um caixa eletrônico.No inicio, pergunte ao usuario o valor  ser sacado (numero inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considerar que o caixa possui cédulas de 50, 20, 10 e 1

print("-="*15)
print("       CAIXA ELETRÔNICO  ")
print("-="*15)

while True:
    cinquenta = 0
    vinte = 0
    dez = 0
    um = 0
    valor = int(input("Digite o valor a ser sacado: "))
    if valor >= 50:
        while valor >= 50:
            valor = valor - 50
            cinquenta += 1
    if valor >= 20:
        while valor >= 20:
            valor = valor - 20
            vinte += 1
    if valor >= 10:
        while valor >= 10:
            valor = valor - 10
            dez += 1
    if valor >= 1:
        while valor >= 1:
            valor = valor - 1
            um += 1
    print("Você receberá:")
    print(f"{cinquenta} cédulas de 50 reais")
    print(f"{vinte} cédulas de 20 reais")
    print(f"{dez} cédulas de 10 reais")
    print(f"{um} cédulas de 1 real")

    resp = str(input("Quer sacar mais? [s/n]"))
    if resp == 'N' or resp == 'n':
        break