

def sumar(lista):
    suma = 0
    for ele in lista:
        suma = suma + ele
    return suma


def multiplicar(lista):
    multiplica = 1
    for ele in lista:
        multiplica = multiplica*ele
    return multiplica


if __name__ == '__main__':

    lista = [1,2,3,4,5]

    command = int(input('Escoge [1]suma, [2]multiplica: '))

    if command == 1:
        s = sumar(lista)
        print('Suma: ', s)
    elif command ==2:
        m = multiplicar(lista)
        print('multiplica: ', m)



