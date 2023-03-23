# Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida,
#  crie uma nova lista que contenha apenas os números que são divisíveis por 3.

lista = []
lista3 = []
for i in range(4):
    lista.append(int(input("Digite um número: ")))
    if lista[i]%3==0:
        lista3.append(lista[i])

print(lista)
print(lista3)
print("")