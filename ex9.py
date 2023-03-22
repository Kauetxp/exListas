# Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números que são menores do que 5.

lista=[]
listaCinco = []
for i in range(4):
    lista.append(int(input("Digite um número: ")))
    if lista[i] < 5:
        listaCinco.append(lista[i])
    
print(listaCinco)