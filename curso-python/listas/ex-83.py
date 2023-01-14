galera = []
dado = [] #estrutura auxiliar
totmai = totmen = 0

for c in range (0,3):
    dado.append(str(input("nome:")))
    dado.append(int(input("idade:")))
    galera.append(dado[:])
    dado.clear() 

for p in galera:
  if p[1] >= 18:
    print (f"{p[0]} é maior de idade")  
    totmai += 1
  else:
    print (f"{p[0]} é maior de idade")   
    totmen += 1

print (f"{totmai} pessoas são maiores de idade e {totmen} menores de idade.")    