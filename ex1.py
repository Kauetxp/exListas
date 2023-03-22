#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números pares da lista.

lista = []

i = 0
while i < 10:
    n = input("Digite um número: ")
    lista.append(n)
    i+=1
print(lista)
