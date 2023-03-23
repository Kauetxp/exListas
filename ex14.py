#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre e imprima o segundo número mais baixo na lista.

lista=[]
for i in range(4):
    lista.append(int(input("Digite um nome: ")))
lista.sort(reverse = True)
print(lista[-2])
