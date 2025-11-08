"""
Solução para o Desafio 07: Sequência de Fibonacci
"""


def fibonacci(n: int) -> list[int]:
    """
    Retorna os primeiros n números da sequência de Fibonacci.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    sequencia = [0, 1]
    
    for i in range(2, n):
        proximo = sequencia[i - 1] + sequencia[i - 2]
        sequencia.append(proximo)
    
    return sequencia


# Testes
if __name__ == "__main__":
    print("Teste 1:", fibonacci(10))
    print("Teste 2:", fibonacci(5))
    print("Teste 3:", fibonacci(1))
    print("Teste 4:", fibonacci(15))

