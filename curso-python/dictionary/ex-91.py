#91
#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um DICIONÁRIO. No final, coloque esse dicionário em ORDEM, sabendo que o vencedror tirou o maior número no dado.

from random import randint
from time import sleep 
from operator import itemgetter #para ordenar por valores em dicionario

jogo = {'jogador 1': randint (1, 6), #gerando numeros aleatorios entre 1 e 6
        'jogador 2': randint (1, 6),
        'jogador 3': randint (1, 6),
        'jogador 4': randint (1, 6)}
ranking = list () #novo lista para por em ordem        

print (f'Valores sorteados: ')    
for k, v in jogo.items():
  print (f'{k} tirou número {v} no dado')   
  sleep (1)  

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #colocar em ordem de valor (ou seja, '1') e reverse para ser do maior para menor
print ('-=' * 30)
print (ranking) 
for i, v in enumerate (ranking): 
  print (f'{i+1}º lugar: {v[0]} com {v[1]}.') #V0 = nome e V1 = pontos // i + 1 para nao começar como 0 lugar, 1 lugar..
  sleep (1)