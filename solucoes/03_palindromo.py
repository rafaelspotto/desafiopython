"""
Solução para o Desafio 03: Verificar Palíndromo
"""


def eh_palindromo(s: str) -> bool:
    """
    Verifica se uma string é um palíndromo, ignorando espaços,
    pontuação e diferenças entre maiúsculas e minúsculas.
    """
    # Remove espaços e converte para minúsculas
    s_limpa = ''.join(c.lower() for c in s if c.isalnum())
    
    # Verifica se é palíndromo
    esquerda = 0
    direita = len(s_limpa) - 1
    
    while esquerda < direita:
        if s_limpa[esquerda] != s_limpa[direita]:
            return False
        esquerda += 1
        direita -= 1
    
    return True


# Testes
if __name__ == "__main__":
    print("Teste 1:", eh_palindromo("A man a plan a canal Panama"))
    print("Teste 2:", eh_palindromo("race a car"))
    print("Teste 3:", eh_palindromo("racecar"))
    print("Teste 4:", eh_palindromo("A Santa at NASA"))

