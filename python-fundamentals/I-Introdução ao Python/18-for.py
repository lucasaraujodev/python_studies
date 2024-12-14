gamesList = ["Fifa", "God of War", "Red Dead 2", "Uncharted"]

# 1 - Iterando valores de uma lista
for list in gamesList:
    print(list)

# 2 - Quando a condição for atendida, o loop será encerrado
for list in gamesList:
    if list == "God of War":
        break
    print(list)

# 3 - Quando a condição for atendida, o loop vai para a próxima iteração
for list in gamesList:
    if list == "God of War":
        continue
    print(list)

# 4 - Avaliação Jogo
gameName = input("Digite o nome do jogo\\n")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo\\n"))

sum = 0
for i in range(gameRating):
    note = float(input("Digite a nota para o jogo \\n"))
    sum += note # sum = sum + note
print(f"Média de avaliação do jogo {gameName} é: {sum/gameRating:.2f}")


