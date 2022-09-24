import datetime

anio_actual = int(input('Año actual: '))

count = 0
while count < 3:
    name = input('Ingresa tu nombre: ')
    nacimiento = int(input('Año de nacimiento: '))
    count += 1

    print('Hola', name, 'cumples', anio_actual-nacimiento,'años')
    print('*'*10)

