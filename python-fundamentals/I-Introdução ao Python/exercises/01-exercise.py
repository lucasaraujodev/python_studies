# 01 - Antecessor e Sucessor de um número:
''' Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse número que foi lido, utilizando operadores de atribuição.
'''
# 02 - Média de 4 notas:
''' Escreva um programa em Python que leia quatro números e calcule a média entre esses números
'''

# RESOLUÇÃO 01
'''
num = int(input("Type a number: "))
a = num - 1
s = num + 1 

print(f"Antecessor: {a}")
print(f"Sucessor: {s}")

# Alternative simpler

number = int(input("Digite um número\\n"))

print(f"Antecessor do número: {number -1} | Sucessor do número: {number +1}")

'''

# RESOLUÇÃO 02
'''
print("Type 4 numbers below:")

num1 = float(input("Type the first number: "))
num2 = float(input("Type the second number: "))
num3 = float(input("Type the third number: "))
num4 = float(input("Type the fourth number: "))

average = (num1 + num2 + num3 + num4) / 4

print(f"The average is {average.2f}")
'''
