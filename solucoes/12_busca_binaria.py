"""
Solução para o Desafio 12: Busca Binária
"""


def busca_binaria(lista: list[int], alvo: int) -> int:
    """
    Implementa busca binária em uma lista ordenada.
    Retorna o índice do alvo se encontrado, ou -1 se não encontrado.
    """
    esquerda = 0
    direita = len(lista) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    
    return -1


# Testes
if __name__ == "__main__":
    print("Teste 1:", busca_binaria([1, 3, 5, 7, 9, 11, 13], 7))
    print("Teste 2:", busca_binaria([1, 3, 5, 7, 9, 11, 13], 4))
    print("Teste 3:", busca_binaria([2, 4, 6, 8, 10], 10))
    print("Teste 4:", busca_binaria([1, 2, 3, 4, 5], 1))

