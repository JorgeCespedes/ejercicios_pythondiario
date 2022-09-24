
lista = ['jodddddddddddddddddddrge','hola amigo','nidia','merida']


def mas_larga(lista):
    numero = 0
    pala = ''
    for palabra in lista:
        if len(palabra) > numero:
            numero = len(palabra)
            pala = palabra
    return pala


larga = mas_larga(lista)

print(larga)

