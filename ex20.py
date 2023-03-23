# Escreva um programa que peça ao usuário para digitar uma lista de palavras e, em seguida, 
# crie uma nova lista que contenha apenas as palavras que têm um número ímpar de letras.

lista = []
listaImpar = []
for i in range(4):
    lista.append(input("Digite uma palavra: "))
    if len(lista[i])%2!=0:
        listaImpar.append(lista[i])

print("\nLista completa:",lista)
print("Palavras com número impar de letras:",listaImpar)
print("")