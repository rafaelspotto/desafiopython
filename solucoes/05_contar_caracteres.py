"""
Solução para o Desafio 05: Contar Caracteres
"""


def contar_caracteres(s: str) -> dict[str, int]:
    """
    Retorna um dicionário com a contagem de cada caractere na string.
    Ignora espaços em branco.
    """
    contagem = {}
    
    for char in s:
        if char != ' ':  # Ignora espaços
            contagem[char] = contagem.get(char, 0) + 1
    
    return contagem


# Testes
if __name__ == "__main__":
    print("Teste 1:", contar_caracteres("hello"))
    print("Teste 2:", contar_caracteres("programming"))
    print("Teste 3:", contar_caracteres("hello world"))

