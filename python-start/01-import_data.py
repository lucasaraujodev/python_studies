# 1 - importing data using pandas
import pandas as pd # giving a nickname for "pandas"

data = pd.read_excel("data/VendaCarros.xlsx")

print(data)

# 2 - firts registers list
print(data.head()) # ao colocar um número x vc escolhe executar os x primeiros, quando não é preenchido ele lista os 5 primeiros

# 3 - last registers list
print(data.tail()) #mesma lógica de "head", porém para os últimos

# 4- contagem de valores x fabricantes
print(data["Fabricante"].value_counts())

