# Uma função lambda (anônima) pode receber qualquer número de argumentos, mas pode ter apenas uma expressão.

# função de potência
power = lambda num: num ** 2

# função de verificação de número par
pair = lambda x: x%2==0

# função de divisão
divNum = lambda x,y : x/y

# função que inverte uma string
reverse = lambda s: s[::-1]

print(power(5))
print(power(9))
print(pair(27))
print(pair(30))
print(divNum(10,2))
print(divNum(7,2))
print(reverse("Função"))
print(reverse("Tecnologia"))