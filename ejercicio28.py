lista_nombres = ['Ann', 'George','Mery','Nidi','Aurely','Rquel','Lin', 'Areli']
def buscar_letra(letra):
    count = 0
    for nombre in lista_nombres:
        if nombre[0].upper() == letra.upper():
            count += 1
    return count


letra = str(input('Ingresa una letra: '))
num_let = buscar_letra(letra)
print(num_let)



