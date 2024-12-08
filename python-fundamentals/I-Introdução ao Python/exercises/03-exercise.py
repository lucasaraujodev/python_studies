# 01 - Cálculo da Distância
''' Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,35 para viagens mais longas.
'''
# 02 - Aumento salário funcionário
''' Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
'''

# RESOLUÇÃO 01
'''distance = float(input('Type the distance (in Km) that you will cover up: '))

if distance <= 200:
    ticket = distance * 0.50
else:
    ticket = distance * 0.35

print(f'The price of your ticket is R$ {ticket:.2f}')
'''
# RESOLUÇÃO 02
'''income = float(input('Type your income (R$): '))

if income > 1250:
    salaryIncrease = (income * 0.1) + income
else:
    salaryIncrease = (income * 0.15) + income
    
print(f'New Salary: R$ {salaryIncrease:.2f}')
# Alternative
salary = float(input("Digite seu salário: "))
perc_increase = 0.15
if salary > 1250:
    perc_increase = 0.10
incresase = salary * perc_increase
print(f"Seu aumento será de: R$ {incresase:.2f}")
'''


