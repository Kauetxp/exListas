#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, calcule e imprima a soma de todos os números ímpares na lista.
lista =[]
listaImpar = []
for i in range(4):
    lista.append(int(input("Digite um número: ")))
    if lista[i]%2!=0:
        listaImpar.append(lista[i])
print(sum(listaImpar))