#atividade - manipulação de lista em python

numeros = [10,20,30,20,40,50]

#1
print("comprimento", len(numeros))

#2
print("quantas vezes 20 aparece:", numeros.count(20))

#3
print("indice de 30:", numeros.index(30))

print("100 estar na lista?", 100 in numeros)

#Crie uma lista chamada numeros com os seguintes valores:

numeros = [91 , 34, 67, 15, 82]
numeros.sort()
print("Apos sorte():", numeros)

#1
numeros.sort(reverse=True)
print("Apos sorte():", numeros)

#crie uma segunda lista chamada dados contendo os numeros:
numeros = [80, 7, 10, 9, 19]

dados = [80,7,10,9,19]
random.shuffle(dados)
print("Embaralhar", dados)
