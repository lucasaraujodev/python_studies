import pandas as pd

# 1 - importing data using pandas
data = pd.read_excel("data/VendaCarros.xlsx")
# print(type(data)) para saber o tipo de dado o pandas retorna para você (dataframe, no caso)

# 2 - Selecting specific columns (dataframe)
# print(data["Estado"])
df = data[["Fabricante", "ValorVenda", "Ano"]]
print(df)

# 3 - creating a pivot table
pivot_table = df.pivot_table(
    index ="Ano",
    columns="Fabricante",
    values="ValorVenda",
    aggfunc="sum"
)

print(pivot_table)

# 4 - exporting pivot table in an excel file
pivot_table.to_excel("data/pivot_table.xlsx", "Relatório")