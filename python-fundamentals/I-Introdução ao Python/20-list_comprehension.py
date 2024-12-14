# A list comprehension oferece uma sintaxe mais curta quando você deseja criar uma nova lista com base nos valores de uma lista existente.
# Sintaxe: newlist = [expression for item in iterable if condition == True]

# 1 - Listando valores de 0 a 10 menores do que 4.
'''
for i in range(10):
    if i < 4:
        print(i)
Ao invés de escrever 3 linhas de código, faça uma:
'''
listNumbers = [x for x in range(10) if x < 4]
print(listNumbers)

# 2 - Jogos que possuam a letra a
gamesList = ["Mario Odyssey", "Donkey Kong Country", "Luigi's mansion", "Kirby"]
"""
Em uma única expressão aplicamos o for e o 
if para selecionar jogos que tenham a letra a

Sintaxe: novalista = 
[expression for item in iterable if condition == True]

"""
newList = [x for x in gamesList if "a" in x]
print(newList)

# 3 - Jogos Zerados
gamesFinished = [x for x in gamesList if x != "Kirby"] 
print(gamesFinished)

