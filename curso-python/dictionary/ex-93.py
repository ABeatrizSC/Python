#93
#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feito em cada partida. No final, tudo será guardado em um dicionário, incluindo o total de gols feito durante o campeonato.

aproveitamento = {}
list_gol = []
tot_gols = v_gol = 0

print('=-'*15)
print("   CALCULAR APROVEITAMENTO  ")
print('=-'*15)
aproveitamento['nome'] = str(input("Nome do jogador: "))
aproveitamento['partidas'] = int(input(f"Quantas partidas {aproveitamento['nome']} jogou? "))
for i in range(0, aproveitamento['partidas']):
    v_gol = int(input(f"Quantidade de gols na {i+1}ª partida: "))
    tot_gols += v_gol
    list_gol.append(v_gol)
aproveitamento['gols'] = list_gol
aproveitamento['totgols'] = tot_gols

print('=-'*15)
print(f"   FICHA DO JOGADOR {aproveitamento['nome']}  ")
print('=-'*15)
print(f"Nome do jogador: {aproveitamento['nome']}")
print(f"Gols marcados: {aproveitamento['gols']}")
print('=-'*15)
print(f"O jogador {aproveitamento['nome']} jogou {aproveitamento['partidas']} partidas.")
for i in range (len(list_gol)):
    print(f"-> Na  {i+1}ª partida ele marcou {list_gol[i]} gols.")
print(f"Total de gols marcados: {tot_gols}")