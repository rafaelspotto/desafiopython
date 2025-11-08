# Desafio 06: Validar Parênteses

## Descrição
Escreva uma função que verifica se uma string contendo apenas os caracteres `(`, `)`, `{`, `}`, `[` e `]` é válida. Uma string é válida se:
- Os parênteses abertos são fechados na ordem correta
- Cada parêntese aberto tem um parêntese fechado correspondente

## Exemplo
```python
validar_parenteses("()")
# Retorna: True

validar_parenteses("()[]{}")
# Retorna: True

validar_parenteses("(]")
# Retorna: False

validar_parenteses("([)]")
# Retorna: False

validar_parenteses("{[]}")
# Retorna: True
```

## Assinatura da Função
```python
def validar_parenteses(s: str) -> bool:
    pass
```

