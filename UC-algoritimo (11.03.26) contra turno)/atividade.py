# Soluções para as 12 questões - atividade

def questao_1():
    base = 3500.0
    bonus = 800.0
    desconto = 250.0
    bruto = base + bonus
    liquido = bruto - desconto
    print("QUESTÃO 1 - Cálculo de Salário")
    print(f"Salário base: R$ {base:.2f}")
    print(f"Bônus: R$ {bonus:.2f}")
    print(f"Salário bruto: R$ {bruto:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Salário líquido: R$ {liquido:.2f}")
    print(f"Tipo das variáveis: base={type(base).__name__}, bonus={type(bonus).__name__}, desconto={type(desconto).__name__}, bruto={type(bruto).__name__}, liquido={type(liquido).__name__}")
    print()


def questao_2():
    distancia = 450.0  # km
    consumo = 8.0      # km por litro
    preco_litro = 5.50 # R$
    litros = distancia / consumo
    custo = litros * preco_litro
    print("QUESTÃO 2 - Cálculo de Consumo de Combustível")
    print(f"Distância percorrida: {distancia} km")
    print(f"Consumo do carro: {consumo} km/l")
    print(f"Preço do litro: R$ {preco_litro:.2f}")
    print(f"Litros consumidos: {litros:.2f} L")
    print(f"Custo total de combustível: R$ {custo:.2f}")
    print()


def questao_3():
    f = 32.0
    c = (f - 32) * 5/9
    print("QUESTÃO 3 - Conversão de Temperatura")
    print(f"Temperatura em Fahrenheit: {f}°F")
    print(f"Temperatura equivalente em Celsius: {c:.2f}°C")
    print()


def questao_4():
    estoque = 100
    print("QUESTÃO 4 - Operadores de Atribuição")
    print(f"Estoque inicial: {estoque}")
    estoque += 50
    print(f"Após receber 50 unidades: {estoque}")
    estoque -= 30
    print(f"Após vender 30 unidades: {estoque}")
    estoque += 5  # devolução
    print(f"Após devolução de 5 unidades: {estoque}")
    print()


def questao_5():
    print("QUESTÃO 5 - Cadastro de Aluno")
    nome = input("Nome completo do aluno: ").strip()
    matricula_str = input("Matrícula (número): ").strip()
    try:
        matricula = int(matricula_str)
    except ValueError:
        print("Matrícula inválida, será registrada como 0.")
        matricula = 0
    nota1_str = input("Nota 1: ").strip()
    nota2_str = input("Nota 2: ").strip()
    try:
        nota1 = float(nota1_str)
    except ValueError:
        nota1 = 0.0
    try:
        nota2 = float(nota2_str)
    except ValueError:
        nota2 = 0.0
    media = (nota1 + nota2) / 2
    print("\n--- Histórico do Aluno ---")
    print(f"Nome: {nome}")
    print(f"Matrícula: {matricula}")
    print(f"Nota 1: {nota1:.2f}")
    print(f"Nota 2: {nota2:.2f}")
    print(f"Média: {media:.2f}")
    print()


def questao_6():
    print("QUESTÃO 6 - Classificação de Idade para Competição")
    try:
        idade = int(input("Idade do atleta: ").strip())
    except ValueError:
        print("Idade inválida. Usando 0.")
        idade = 0
    if idade < 12:
        categoria = 'Infantil'
    elif 12 <= idade < 18:
        categoria = 'Juvenil'
    elif 18 <= idade < 60:
        categoria = 'Adulto'
    else:
        categoria = 'Sênior'
    print(f"Categoria: {categoria}")
    print(f"Bem-vindo(a), atleta de {idade} anos!")
    print()


def questao_7():
    print("QUESTÃO 7 - Validação de Senha")
    senha = input("Digite uma senha: ")
    tem_tamanho = len(senha) >= 8
    tem_numero = any(ch.isdigit() for ch in senha)
    if tem_tamanho and tem_numero:
        print("Senha válida.")
    else:
        print("Senha inválida. Deve ter pelo menos 8 caracteres e conter ao menos um número.")
    print()


def questao_8():
    print("QUESTÃO 8 - Cálculo de Desconto Progressivo")
    try:
        valor = float(input("Valor da compra (R$): ").strip())
    except ValueError:
        print("Valor inválido. Usando 0.")
        valor = 0.0
    if valor < 100:
        taxa = 0.0
    elif valor < 500:
        taxa = 0.05
    elif valor < 1000:
        taxa = 0.10
    else:
        taxa = 0.15
    desconto = valor * taxa
    total = valor - desconto
    print(f"Valor original: R$ {valor:.2f}")
    print(f"Desconto ({taxa*100:.0f}%): R$ {desconto:.2f}")
    print(f"Valor final: R$ {total:.2f}")
    print()


def questao_9():
    print("QUESTÃO 9 - Contagem Regressiva")
    contador = 10
    while contador >= 0:
        print(contador)
        contador -= 1
    print("Foguete lançado!")
    print()


def questao_10():
    print("QUESTÃO 10 - Tabuada Customizável")
    try:
        n = int(input("Digite um número inteiro para ver a tabuada: ").strip())
    except ValueError:
        print("Entrada inválida. Usando 1.")
        n = 1
    for i in range(1, 11):
        print(f"{n} × {i} = {n * i}")
    print()


def questao_11():
    print("QUESTÃO 11 - Soma de Números Pares")
    soma = 0
    for i in range(1, 101):
        if i % 2 == 0:
            soma += i
    print(f"Soma dos números pares de 1 a 100: {soma}")
    print()


def questao_12():
    print("QUESTÃO 12 - Leitura com Validação")
    total = 0.0
    transacoes = 0
    while True:
        try:
            entrada = float(input("Digite o valor do depósito (0 para encerrar): ").strip())
        except ValueError:
            print("Valor inválido. Tente novamente.")
            continue
        if entrada == 0.0:
            break
        total += entrada
        transacoes += 1
    print(f"Total de depósitos: R$ {total:.2f}")
    print(f"Quantidade de transações: {transacoes}")
    print()


def main():
    questao_1()
    questao_2()
    questao_3()
    questao_4()
    # As próximas questões pedem interação com o usuário
    questao_5()
    questao_6()
    questao_7()
    questao_8()
    questao_9()
    questao_10()
    questao_11()
    questao_12()


if __name__ == '__main__':
    main()