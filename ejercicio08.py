
lista1 = [1,2,3]
lista2 = [6,4,5]

def superposicion(lista1, lista2):
    for l1 in lista1:
        #print('loop1: ', l1)
        for l2 in lista2:
            if l1 == l2:
                return True


sup = superposicion(lista1, lista2)
if sup == True:
    print('Comun')
else:
    print('No comun')
