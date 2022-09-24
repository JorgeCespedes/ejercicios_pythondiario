
def max_de_tres(n1, n2, n3):
    mayor = []
    mayor.append(n1)
    mayor.append(n2)
    mayor.append(n3)

    maximo=max(mayor)

    return maximo



if __name__ == '__main__':
    n1=int(input('Primer número: '))
    n2=int(input('Segundo número: '))
    n3=int(input('Tercero número: '))

    mayor = max_de_tres(n1,n2,n3)

    print('El número mayor es: '+str(mayor))

