
cadena = input('Add cadena: ')

count = 0
for c in cadena:
    if c == c.upper():
        count += 1
print('Número de mayusculas', count)
