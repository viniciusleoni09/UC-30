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

        # Ler os dois valores
        def ler_valor(prompt):
            while True:
                entrada = input(prompt).strip()
                # permite usar vírgula como separador decimal
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
        else:  # opcao == '4'
            if b == 0:
                print('Erro: divisão por zero não é permitida.')
                continue
            resultado = a / b
            operador = '/'

        # Exibir resultado com remoção de .0 quando inteiro
        def formato_num(n):
            if n == int(n):
                return str(int(n))
            return str(n)

        print(f'Resultado: {formato_num(a)} {operador} {formato_num(b)} = {formato_num(resultado)}')


if __name__ == '__main__':
    calculadora()