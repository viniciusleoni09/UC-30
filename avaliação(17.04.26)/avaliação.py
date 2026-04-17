#questão 1
print("hello world")

#questão 2 
idade = int(input("Digite sua idade: "))
if idade >= 16:
    print("pode votar!")
else:
    print("ainda não pode votar>")

#questão 3
valor = float(input("digite o valor do item (0 para sair):"))
while valor != 0:
    total += valor
    valor = float(input("digite o valor do item (0 para sair):"))
print(f"total final R$ {total:.2f}")

#questão 4
def categoriza_imc():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros:"))
    if imc < 18.5:
        print(f"IMC: {imc:.2f} magro" )
    elif imc <= 24.9:
        print(f"IMC: {imc:.2f} normal")
    else:
        print(f"IMC: {imc:.2f} acima do peso")

#questão 5     
nomes = input("Digite os nomes dos amigos separados por virgula:") .split(',')
quantidade = len(nomes)
print(f"quantidade de amigos: {quantidade}")
if quantidade % 2 == 0:
    print("a quantidade e par")
else:
    print("a quantidade e impar")


#questão 6
print ("digite as 7 temperaturas diarias da semana:")
temperaturas = []
for i in range(7):
    temp = float(input(f"Temperatura do dia {i+1}: "))
    temperaturas.append(temp)
    media = sum(temperaturas) / 7
    print(f"Média das temperaturas: {media:.2f}")


#questão 7
vendas = input("Digite os numeros de vendas separados por virgulas:").split(',')
vendas = [int(v.strip()) for v in vendas]
soma_pares = 0
for valor in vendas:
    if valor % 2 == 0:
        soma_pares += valor
        print(f"soma dos valores pares: {soma_pares}")


#questão 8
valor = float(input("Digite o valor da compra: R$"))
if valor > 500:
    preço_final = valor * 0.8
elif valor >= 200:
    preço_final = valor * 0.9
else:
    preço_final = valor
    print(f"preço final com desconto: R$ {preço_final:.2f}")


#questão 9
notas = input("Digite as notas dos alunos separadas por virgula: ").split(',')
notas = [float(n.stip()) for n in notas]
acima_de_sete = 0
for nota in notas:
    if nota > 7:
        acima_de_sete += 1
        print(f"quantidade de notas acima de 7: {acima_de_sete}")



 #questão 12
 def calculadora():
    """Calculadora simples em loop com opções: soma, subtração, multiplicação, divisão e sair."""
    while True:
        print('\n=== Calculadora ===')
        print('1 - Soma')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        print('5 - Sair')

        opcao = input('Escolha uma opção (1-5): ').strip()

        if opcao == '5':
            print('Encerrando a calculadora. Até logo!')
            break

        if opcao not in {'1', '2', '3', '4'}:
            print('Opção inválida. Tente novamente.')
            continue

        
        def ler_valor(prompt):
            while True:
                entrada = input(prompt).strip()
                
                entrada = entrada.replace(',', '.')
                try:
                    return float(entrada)
                except ValueError:
                    print('Valor inválido. Digite um número válido.')

        a = ler_valor('Digite o primeiro valor: ')
        b = ler_valor('Digite o segundo valor: ')

        if opcao == '1':
            resultado = a + b
            operador = '+'
        elif opcao == '2':
            resultado = a - b
            operador = '-'
        elif opcao == '3':
            resultado = a * b
            operador = '*'
        else:  
            if b == 0:
                print('Erro: divisão por zero não é permitida.')
                continue
            resultado = a / b
            operador = '/'

        
        def formato_num(n):
            if n == int(n):
                return str(int(n))
            return str(n)

        print(f'Resultado: {formato_num(a)} {operador} {formato_num(b)} = {formato_num(resultado)}')


if __name__ == '__main__':
    calculadora()       
