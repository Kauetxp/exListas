#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, calcule a média dos números na lista.

lista = []

for i in range(5):
    lista.append(int(input("Digite um número: ")))

media = sum(lista)/len(lista)
print(media)


