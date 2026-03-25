 

from typing import Iterable, Optional, Dict
import sys


def resumo_notas(notas: Iterable) -> Optional[Dict[str, float]]:
    
    
    notas_float = []
    for n in notas:
        try:
            notas_float.append(float(n))
        except (ValueError, TypeError):
            continue

    if not notas_float:
        return None

    s = sum(notas_float)
    qtd = len(notas_float)
    return {
        'soma': s,
        'media': s / qtd,
        'maior': max(notas_float),
        'menor': min(notas_float),
        'quantidade': qtd,
    }


if __name__ == '__main__':

    args = sys.argv[1:]
    resumo = resumo_notas(args)
    if resumo is None:
        print('Nenhuma nota válida fornecida.')
    else:
        print('Resumo das notas:')
        print(f"Soma: {resumo['soma']}")
        print(f"Média: {resumo['media']}")
        print(f"Maior: {resumo['maior']}")
        print(f"Menor: {resumo['menor']}")
        print(f"Quantidade: {resumo['quantidade']}")
