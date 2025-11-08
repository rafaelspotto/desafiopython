"""
Solução para o Desafio 09: Remover Duplicatas
"""


def remover_duplicatas(lista: list[int]) -> list[int]:
    """
    Remove elementos duplicados mantendo a ordem original,
    sem usar set() ou métodos similares.
    """
    resultado = []
    vistos = []
    
    for elemento in lista:
        if elemento not in vistos:
            resultado.append(elemento)
            vistos.append(elemento)
    
    return resultado


# Testes
if __name__ == "__main__":
    print("Teste 1:", remover_duplicatas([1, 2, 2, 3, 4, 4, 5]))
    print("Teste 2:", remover_duplicatas([3, 3, 3, 3]))
    print("Teste 3:", remover_duplicatas([1, 1, 2, 2, 3, 3]))
    print("Teste 4:", remover_duplicatas([5, 2, 3, 2, 1, 5, 4]))

