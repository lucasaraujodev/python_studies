# Módulo de Strings
'''
Escreva um módulo em python para tratar algumas strings e que possua as seguintes funcionalidades:

1. Inverter uma string de trás pra frente.
2. Retornar apenas letras com índice par.
3. Retornar apenas letras com índice ímpar.
'''
# RESOLUÇÃO

import strings

message = "Hello World"

print(strings.inverse(message))
print(strings.even_characters(message))
print(strings.odd_characters(message))