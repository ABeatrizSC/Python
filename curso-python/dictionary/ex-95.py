#95
#Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
#do aproveitamento do jogador.

aproveitamento = {} #Dicionário
list_gol = [] #Lista para armazenar apenas os gols, separados por cada partida
lista = [] #Lista para guardar os dados após os dicionários


print('=-'*15)
print("   CALCULAR APROVEITAMENTO  ")
print('=-'*15)
while True:
    tot_gols = v_gol = 0
    aproveitamento['nome'] = str(input("Nome do jogador: "))
    aproveitamento['partidas'] = int(input(f"Quantas partidas {aproveitamento['nome']} jogou? "))
    for i in range(0, aproveitamento['partidas']):
        v_gol = int(input(f"Quantidade de gols na {i+1}ª partida: "))
        tot_gols += v_gol #total de gols recebe os gols de cada partida
        list_gol.append(v_gol) #Lista de gols recebe os valores de gol por partida
    aproveitamento['gols'] = list_gol[:] #Copia-se a Lista com todos os gols por partida para o dicionário
    aproveitamento['totgols'] = tot_gols #Copia-se o total de gols para o dicionário também
    lista.append(aproveitamento.copy()) #Lista irá receber Dicionário 'aproveitamento' (completo)
    aproveitamento.clear() #Limpar dados do Dicionário 'aproveitamento'
    list_gol.clear() #Limpar dados da Lista de gols
    resp = str(input("Quer continuar? [s/nª]"))
    if resp in ('Nn'):
        break
print('=-'*15)
print(f"Cod     Nome     Gols      Total de gols ")
for v in range (0, len(lista)): #Para cada valor de 0 até o comprimento da lista, faça:
    print(f"{v+1}      {lista[v]['nome']}     {lista[v]['gols']}        {lista[v]['totgols']}") #Cabeçalho da tabela
print('=-'*15)


while True:
    dados = int(input("Mostrar dados de qual jogador? (utilize seu cod/999 para parar) ")) #dados recebe o cod do jogador (seu índice)
    if dados == 999:
        print("Processo encerrado.")
        break
    while dados > len(lista): #Enquanto o número informado for maior que o existente na lista.
        print("ERRO! Não há jogadores com o código informado. Digite novamente!")
        dados = int(input("Mostrar dados de qual jogador? (utilize seu cod/999 para parar) "))

    dados = dados - 1
    print('=-' * 15)
    print(f"=-=LEVANTAMENTO DE DADOS: {lista[dados]['nome']} =-=")
    print('=-' * 15)
    lista_gol = lista[dados]['gols'] #Lista de gols volta a ser usada para mostrar só os gols em cada partida
    for i in range(0, lista[dados]['partidas']): #Para i de 0 até o numero de partidas, faça:
        print(f"No {i+1}º jogo fez {list_gol[i]} gols.") #No (numero do indice + 1 para ficar certo)
        # jogo fez (lista de gols em cada partida determinado pelo índice 'i'. Jogo 1: indice 0, jogo 2: indice 1)
    print('=-'*15)