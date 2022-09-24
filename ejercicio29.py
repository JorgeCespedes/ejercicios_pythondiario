
def contar_vocales(palabra):
    vocales = ['a','e','i','o','u']
    count = 0
    for pal in palabra:
        for vocal in vocales:
            if pal == vocal:
                count += 1
    return count



palabra = str(input('Ingraesa una palabra: '))

cv = contar_vocales(palabra)

print(cv)
