def is_palindromo(texto):
    #texto = texto.split()
    if texto == texto[::-1]:
        return True
    else:
        return False


def palabra():
    texto = input('Ingresa una palabra: ')
    pali = is_palindromo(texto)
    if pali == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


palabra()

