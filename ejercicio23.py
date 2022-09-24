
lista = ['jorge', 'nidia', 'hola', 'merida']
n = 4
# jorge, nidia

def filtrar_palabras(lista, n):
    palabbras = []
    for l in lista:
        if len(l) > n:
            palabbras.append(l)
    return palabbras




fp = filtrar_palabras(lista,n)

print(fp)
