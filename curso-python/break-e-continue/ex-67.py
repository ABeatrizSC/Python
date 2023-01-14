#67
#Faça um programa que mostre a tabuada de varios numeros, um de cada vez. O programa será interrompido quando o número solicitado for negativo.

tabuada = 0
multi = 1
print('-='*10)
print("      " + "TABUADA" + "    ")
print('-='*10)
while True:
  num = int(input("Digite o numero: "))
  if num > 0:
    while multi <= 10:
      tabuada = num * multi
      print(f"{num} x {multi} = {tabuada}", " ")
      multi += 1
  else: 
      break 
     