"""
Solução para o Desafio 10: Verificar Anagramas
"""


def sao_anagramas(s1: str, s2: str) -> bool:
    """
    Verifica se duas strings são anagramas, ignorando espaços,
    pontuação e diferenças entre maiúsculas e minúsculas.
    """
    # Remove espaços, pontuação e converte para minúsculas
    def limpar_string(s: str) -> str:
        return ''.join(c.lower() for c in s if c.isalnum())
    
    s1_limpa = limpar_string(s1)
    s2_limpa = limpar_string(s2)
    
    # Se os tamanhos são diferentes, não são anagramas
    if len(s1_limpa) != len(s2_limpa):
        return False
    
    # Conta os caracteres de cada string
    contagem1 = {}
    contagem2 = {}
    
    for char in s1_limpa:
        contagem1[char] = contagem1.get(char, 0) + 1
    
    for char in s2_limpa:
        contagem2[char] = contagem2.get(char, 0) + 1
    
    return contagem1 == contagem2


# Testes
if __name__ == "__main__":
    print("Teste 1:", sao_anagramas("listen", "silent"))
    print("Teste 2:", sao_anagramas("The Morse Code", "Here come dots"))
    print("Teste 3:", sao_anagramas("hello", "world"))
    print("Teste 4:", sao_anagramas("rail safety", "fairy tales"))

