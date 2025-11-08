"""
Solução para o Desafio 11: Fatorial
"""


def fatorial(n: int) -> int:
    """
    Calcula o fatorial de um número usando recursão.
    """
    if n < 0:
        raise ValueError("Fatorial não está definido para números negativos")
    
    # Caso base
    if n == 0 or n == 1:
        return 1
    
    # Caso recursivo
    return n * fatorial(n - 1)


# Testes
if __name__ == "__main__":
    print("Teste 1:", fatorial(5))
    print("Teste 2:", fatorial(0))
    print("Teste 3:", fatorial(3))
    print("Teste 4:", fatorial(7))

