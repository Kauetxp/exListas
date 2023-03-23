#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, 
# crie uma nova lista que contenha apenas os nomes que contêm a letra "e".

lista = []
listaE = []
for i in range(4):
    n = input("Digite um nome: ")
    n = n.upper()
    lista.append(n)

for i2 in range(4):
    palavra = lista[i2]
    cLetra = len(palavra)
    for i3 in range(cLetra):
        if palavra[i3] == "E":
            listaE.append(palavra)

print(lista)
print(listaE)
print("")