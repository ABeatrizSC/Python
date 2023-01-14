#Crie um programa que use um loop while e pede continuamente ao utilizador para introduzir uma palavra, a menos que o utilizador introduza "parar" como a palavra secreta de saída, caso em que a mensagem "You've successfully left the loop." deve ser impressa para o ecrã, e o loop deve terminar.

while True:
   palavra = str (input("Digite uma palavra:"))
   if palavra == 'parar':
       break

print ("You've successfully left the loop.")  
     