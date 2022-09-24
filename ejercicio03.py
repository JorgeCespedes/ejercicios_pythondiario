
def largo_lista(lista):
    count = 0
    for i in lista:
        count += 1
    return count


if __name__ == '__main__':
    my_lista = [1,2,3,4,5, 't', 'r']

    lista = largo_lista(my_lista)

    print('largo lista: ', str(lista))

