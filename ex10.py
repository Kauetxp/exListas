#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima a lista com os números duplicados removidos.

lista =[]
for i in range(4):
    lista.append(int(input("Digite um número: ")))

lista = list(set(lista))
lista.sort()
print(lista)

