#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números pares da lista.

lista = []
listaPar = []
i = 0
while i < 5:
    n = int(input("Digite um número: "))
    lista.append(n)
    if n%2==0:
        listaPar.append(n)
    i+=1

print("Os números pares digitados foram:",listaPar)