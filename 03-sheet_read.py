# no openpyxl, primeiro você declara o arquivo (workbook) e depois a planilha (sheet) que se quer trabalhar
from openpyxl import load_workbook

# 1- Ler pasta de trabalho e planilha
wb = load_workbook("data/pivot_table.xlsx")
sheet = wb["Relatório"]
# print(wb)
# print(sheet)

# 2 - Acessando um valor de uma célula específica (manualmente)
# print(sheet["A3"].value)
# print(sheet["B3"].value) 

# 3 - iterando valores por loop - fazer o mesmo que acima de forma automatizada
for i in range (2, 6): # "range" imprime um intervalo de valores, lembrando que o último item será excluído
    # print(i)
    ano = sheet["A%s" %i].value
    # print(ano)
    am = sheet["B%s" %i].value # Aston Martin
    bt = sheet["C%s" %i].value # Bentley
    print("{0} o Anton Martin vendeu {1} e o Bentley vendeu {2}".format(ano, am, bt)) # {0}, {1}, {2} tornaram-se o ano/ValorVenda usando o format