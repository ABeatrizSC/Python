#90
#faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

situacao = dict ()

situacao ['nome'] = str (input('Nome: '))
situacao ['media'] = float (input(f'Média de {situacao["nome"]} : '))
print ("=-" * 15)
print (f'Nome do aluno: {situacao["nome"]}')
print (f'Média do aluno: {situacao["media"]}')
if situacao["media"] > 6:
  print ("Aluno aprovado!")
else:
  print ("Aluno reprovado!")  