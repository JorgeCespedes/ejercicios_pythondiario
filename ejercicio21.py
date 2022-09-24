def max_in_list(lista):
    numero = 0
    for n in lista:
        if n > numero:
            numero = n
    else:
        return numero



lista =[12,8,5,6]

mayor = max_in_list(lista)

print('El mayor es: ', mayor)
