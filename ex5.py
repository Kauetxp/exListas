# Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima a lista ordenada em ordem crescente.

lista = []

for i in range(4):
    lista.append(int(input("Digite um número: ")))
lista.sort()
print(lista)



