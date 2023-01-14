#26
#Faça um programa que leia uma frase pelo teclado e mostre:
#a) quantas vezes aparece a letra “A”
#b) em que posição ela aparece a primeira vez.
#c) em que posição ela aparece a última vez

frase = str(input("Digite uma frase: ")).strip()
frase = frase.upper() 
print("A letra A aparee na frase {} vezes".format(frase.count('A')))
print("A letra A aparece a primeira vez na posição {}".format(frase.find('A')+1)) 
print("A última letra A aparece na posição {}".format(frase.rfind('A')+1)) #analisar a partir da DIREITA