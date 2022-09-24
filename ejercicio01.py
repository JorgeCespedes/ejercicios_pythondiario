def max(n1, n2):
    if n1>n2:
        return 'El mayor es {}'.format(n1)
    elif n1<n2:
        return 'El mayor es {}'.format(n2)
    else:
        return 'Ninguna es mayor'


if __name__ == '__main__':
    n1=int(input('Primer número: '))
   
    n2=int(input('Segundo número: '))
   
    mayor = max(n1,n2)

    print(mayor)
