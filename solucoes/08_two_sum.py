"""
Solução para o Desafio 08: Two Sum
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Retorna os índices dos dois números que somados resultam no alvo.
    """
    # Usa um dicionário para armazenar o valor e seu índice
    mapa = {}
    
    for i, num in enumerate(nums):
        complemento = target - num
        
        if complemento in mapa:
            return [mapa[complemento], i]
        
        mapa[num] = i
    
    return []


# Testes
if __name__ == "__main__":
    print("Teste 1:", two_sum([2, 7, 11, 15], 9))
    print("Teste 2:", two_sum([3, 2, 4], 6))
    print("Teste 3:", two_sum([3, 3], 6))
    print("Teste 4:", two_sum([1, 5, 3, 9, 2], 7))

