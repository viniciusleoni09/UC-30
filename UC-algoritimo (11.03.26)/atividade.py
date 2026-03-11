
aluno = {}
aluno['nome'] = input('Nome do aluno: ')
aluno['nota1'] = float(input('Nota da prova 1: '))
aluno['nota2'] = float(input('Nota da prova 2: '))


total = aluno['nota1'] + aluno['nota2']
aluno['media'] = total / 2


def situacao(media):
    if media >= 7:
        return 'Aprovado'
    elif 5 <= media < 7:
        return 'Recuperação'
    else:
        return 'Reprovado'

aluno['situacao'] = situacao(aluno['media'])


for chave, valor in aluno.items():
    print(f'{chave}: {valor}')
