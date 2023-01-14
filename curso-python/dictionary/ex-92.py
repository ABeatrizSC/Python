#92

#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre (com a idade) em um dicionário se for. Se por acaso a CTPS for diferente de zero, o dicionário considerado também o ano de contratação e o salário.
#Calcule e acrescente além da idade com quantos anos a pessoa vai se aposentar

dados = {}

dados['nome'] = str(input("Nome: "))
ano = int(input("Ano de nascimento: "))
dados['idade'] = int(2022 - ano)
dados['ctps'] = int(input("Carteira de trabalho (Digite 0 se não tiver): "))
if dados['ctps'] != 0:
    dados['ano_contrat'] = int(input("Ano de contatação: "))
    dados['salario'] = float(input("Salário: "))
    dados['aposent'] = int(((ano - dados['ano_contrat'])*-1)+ 35)
print(f"Nome:{dados['nome']}")
print(f"Idade:{dados['idade']}")
if dados['ctps'] == 0:
    print(f"CTPS nº:NÃO POSSUI")
if dados['ctps'] != 0:
    print(f"Ano de contratação:{dados['ano_contrat']}")
    print(f"Você irá se aposentar com {dados['aposent']} anos.")