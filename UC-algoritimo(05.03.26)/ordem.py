import random

numeros = [45,12,78,23,56]
print("Lista oficial:", numeros)

#sorte crescente
numeros.sort()
print("Apos sorte():", numeros)

numeros.sort(reverse=True)
print("Apos sorte():", numeros)

dados = [1,2,3,4,5]
random.shuffle(dados)
print("Embaralhar", dados)
