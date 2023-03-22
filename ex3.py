# Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre o número máximo e o número mínimo da lista.

lista =[]
maior = 0
menor = 99999999

for i in range(4):
    lista.append(int(input("Digite um número: ")))

for i2 in range(4):
    if lista[i2] > maior:
        maior = lista[i2]
    if lista[i2] < menor:
        menor = lista[i2]

print("O maior número é: ",maior,"\nO menor número é: ",menor)