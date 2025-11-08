"""
Solução para o Desafio 06: Validar Parênteses
"""


def validar_parenteses(s: str) -> bool:
    """
    Verifica se uma string contendo parênteses, colchetes e chaves é válida.
    """
    pilha = []
    pares = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in pares.values():  # Caractere de abertura
            pilha.append(char)
        elif char in pares:  # Caractere de fechamento
            if not pilha or pilha.pop() != pares[char]:
                return False
    
    return len(pilha) == 0


# Testes
if __name__ == "__main__":
    print("Teste 1:", validar_parenteses("()"))
    print("Teste 2:", validar_parenteses("()[]{}"))
    print("Teste 3:", validar_parenteses("(]"))
    print("Teste 4:", validar_parenteses("([)]"))
    print("Teste 5:", validar_parenteses("{[]}"))

