# 01 - Contagem Regressiva
'''Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”.
'''
# 02 - Tabuada
''' Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário'''

# RESOLUÇÃO 01
'''
countdown = 11
while countdown > 0:
    countdown -= 1
    print(countdown)
print("beep.")

#Alternative

import winsound
x = 10
while x >= 0:
    print(x)
    x =- 1
winsound.Beep(2500, 500)
'''
# RESOLUÇÃO 02
'''
number = int(input("Tabuada de: "))
begin = int(input("De: "))
end = int(input("Até: "))
x = begin
while x <= end:
    print(f"{number} x {x} = {number * x}")
    x = x + 1
'''


