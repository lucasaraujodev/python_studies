#Utilizar funções pode ser uma boa opção a fim de reaproveitar a execução de blocos sem a necessidade de duplicação de código. E utilizar funções com argumentos (parâmetros), torna ainda mais dinâmica a sua utilização.

def full_name(fname, lname):
    print(f"{fname} {lname}")
full_name("Nathaly", "Araújo")

def sum(a, b):
    print(a + b)
sum(2, 4)

def address(country="Brasil"):
    print(f"Eu moro no {country}")
address()
address("Canadá") #É possível sobrescrever o valor doo argumento original

def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo\\n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo \\n"))
        sum += note
    print(f"Média de avaliação do jogo {game_name} é: {sum/qtdRating}")

rating = int(input("Digite quantas avaliações deseja fazer no jogo\\n"))
rating_game(rating)
