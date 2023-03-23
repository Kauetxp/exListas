#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, 
# crie uma nova lista que contenha apenas os números que aparecem mais de uma vez na lista original.

lista =[]
for i in range(4):
    lista.append(int(input("Digite um número: ")))
lista2 = []
lista3 = []
for i2 in range(4):
    if lista[i2] not in lista2:
        lista2.append(lista[i2])
    else:
        lista3.append(lista[i2])

print("O número que repete é o:",lista3)


