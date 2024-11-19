# 01 - Substituindo caractere repetido:
''' Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere (repetido) foram alteradas para '$', exceto o próprio primeiro caractere
  Ex:
    fifa 23 → fi#a 23
    restart→ resta#t
'''
# 02 - Troca de caracteres:
''' Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e troque os dois primeiros caracteres de cada string.
  Ex:
    abc xyz → xyc abz
'''

# RESOLUÇÃO 01
name = 'Fifa 23'

character = name[0].lower()
new = name.replace(character, '#')
new = character +  new[1:]
print(new)

# RESOLUÇÃO 02
word1 = input("type any word:")
word2 = input("Type another word:")

newWord1 = word1.replace(word1[0:2], word2[0:2])
newWord2 = word2.replace(word2[0:2], word1[0:2])

print(f"Inserted words: {word1} and {word2}" )
print(f"New words: {newWord1} and {newWord2}")
# Alternative
st1 = 'abc'
st2 = 'xyz'

new_st1 = st2[:2] + st1[2:]
new_st2 = st1[:2] + st2[2:]

print(f"{new_st1} {new_st2}")