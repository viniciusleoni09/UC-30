import random


numero_secreto = random.randint(1, 100)
tentativas = 0
while True:
    palpite = int(input("Adivinhe o número entre 1 e 100: "))
    tentativas += 1
    if palpite < numero_secreto:
        print("maior")
    elif palpite > numero_secreto:
        print("menor")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break


numeros = []
for i in range(8):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)


repetidos = {}
for n in numeros:
    if numeros.count(n) > 1:
        repetidos[n] = numeros.count(n)

if repetidos:
    print("Números repetidos e suas quantidades:")
    for num, qtd in repetidos.items():
        print(f"Número {num} apareceu {qtd} vezes.")
else:
    print("Nenhum número foi repetido.")
