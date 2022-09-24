
def binario_a_entero(binario):
    entero = 0
    binario = str(binario)
    rango = len(binario)-1
    i=0
    for bi in binario:
        entero += int(bi)*2**(rango+i)
        i=i-1
    return entero



be = binario_a_entero(111)

print(be)


