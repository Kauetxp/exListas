# Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, imprima o nome mais longo e o nome mais curto da lista.

lista=[]

for i in range(4):
    lista.append(input("Digite um nome: "))
lmaior = max(lista,key=len)
lmenor = min(lista,key=len)

print("Esse é o maior nome:",lmaior)
print("Esse é o menor nome:",lmenor)

