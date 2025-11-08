"""
Solução para o Desafio 04: Encontrar Maior Elemento
"""


def maior_elemento(lista: list[int]) -> int:
    """
    Retorna o maior elemento de uma lista sem usar a função max().
    """
    if not lista:
        raise ValueError("Lista vazia")
    
    maior = lista[0]
    
    for elemento in lista[1:]:
        if elemento > maior:
            maior = elemento
    
    return maior


# Testes
if __name__ == "__main__":
    print("Teste 1:", maior_elemento([3, 7, 2, 9, 1, 5]))
    print("Teste 2:", maior_elemento([-10, -5, -20, -1]))
    print("Teste 3:", maior_elemento([42]))
    print("Teste 4:", maior_elemento([1, 2, 3, 4, 5]))

