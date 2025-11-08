"""
Solução para o Desafio 01: FizzBuzz
"""


def fizzbuzz(n: int) -> list[str]:
    """
    Retorna uma lista de strings de 1 até n, onde:
    - Números divisíveis por 3 são substituídos por "Fizz"
    - Números divisíveis por 5 são substituídos por "Buzz"
    - Números divisíveis por ambos são substituídos por "FizzBuzz
    """
    resultado = []
    
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            resultado.append("FizzBuzz")
        elif i % 3 == 0:
            resultado.append("Fizz")
        elif i % 5 == 0:
            resultado.append("Buzz")
        else:
            resultado.append(str(i))
    
    return resultado


# Testes
if __name__ == "__main__":
    print("Teste 1:", fizzbuzz(15))
    print("Teste 2:", fizzbuzz(5))
    print("Teste 3:", fizzbuzz(30))

