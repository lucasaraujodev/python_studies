# O set é usado para armazenar vários itens em uma única variável.
# Além disso, é importante ressaltar que no set, utilizamos as chaves. Diferentemente de outros tipos, o set não permite recuperar valores via fatiamento.
# Não possibilita recuperar valores no set via slice

gamesSet = {"Fifa23", "Red Dead 2", "Star Wars", "The Legend of Zelda", "Red Dead 2"}
print(gamesSet)
print(len(gamesSet))

# 1 - True e 1 são considerados o mesmo valor
exampleSet = {"Fifa23", True, 1, 90.50} 
print(exampleSet)

# 2 - Adicionando item no set
gamesSet.add("Resident Evil 4")
print(gamesSet)

# 3 - Adicionando item de outro set
gamesSet.update(exampleSet)
print(gamesSet)

# 4 - Remove um item no set
gamesSet.remove(True)
gamesSet.remove(90.5)
print(gamesSet)

