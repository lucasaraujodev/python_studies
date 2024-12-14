# Utilizar funções pode ser uma boa opção a fim de reaproveitar a execução de blocos sem a necessidade de duplicação de código.
# A palavra reservada def é utilizada para criação de uma função.

def welcome():
    print("Hello World")

def create_game():
    name = input("Digite o nome do jogo \\n")
    yearLaunch = int(input("Digite o ano de lançamento\\n"))
    gamePrice = float(input("Digite o preço do jogo\\n"))
    noteRating = float(input("Digite a nota de avaliação do jogo\\n"))
    print(name)
    print(yearLaunch)
    print(gamePrice)
    print(noteRating)

welcome()
create_game()