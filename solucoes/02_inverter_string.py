"""
Solução para o Desafio 02: Inverter String
"""


def inverter_string(s: str) -> str:
    """
    Inverte uma string sem usar métodos built-in como reverse() ou [::-1].
    """
    resultado = ""
    
    # Percorre a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    
    return resultado


# Testes
if __name__ == "__main__":
    print("Teste 1:", inverter_string("Python"))
    print("Teste 2:", inverter_string("Hello World"))
    print("Teste 3:", inverter_string("12345"))

