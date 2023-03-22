#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números que são maiores do que 10.

lista=[]
listaMaiorDez = []
for i in range(4):
    lista.append(int(input("Digite um número: ")))
    if lista[i] > 10:
        listaMaiorDez.append(lista[i])
    

print(listaMaiorDez)

