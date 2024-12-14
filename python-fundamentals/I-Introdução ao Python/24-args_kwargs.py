'''
Utilizamos o *args quando não temos a certeza de quantos argumentos vamos ter dentro de uma função. Ao utilizá-lo, deixamos essa informação dinâmica e variável. Os argumentos são passados como uma tupla.

Utilizamos o **kwargs para passar além dos valores, as respectivas chaves para os seus argumentos. Os argumentos são passados como um dicionário (como pares chave:valor).
'''
def sum(*num):
    sum_total = 0
    
    for n in num:
        sum_total = sum_total + n

    print(f"Soma é: {sum_total}")
sum(7)
sum(8, 7)
sum(4, 5, 9)
sum(6, 8, 3, 1)

def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
print("######Curso######")
presentation(name="Python", category="Backend", level="Iniciante")