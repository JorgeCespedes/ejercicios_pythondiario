
def es_bisiesto(anio):
    if anio % 4 == 0 and anio % 10 != 0:
        return 'Es bisiesto'
    else:
        return 'No es bisiesto'


anio = int(input('Ingresa un año '))
eb = es_bisiesto(anio)

print(eb)
