#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima a lista com os números duplicados removidos.

lista =[]
for i in range(4):
    lista.append(int(input("Digite um número: ")))
lista2 =[]
for i2 in range(4):
    if lista[i2] not in lista2:
        lista2.append(lista[i2])
print(lista)        
print(lista2)
