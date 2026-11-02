# -*- coding: utf-8 -*-

def aplicar_a_cada_elemento(lista, funcion):
    '''
    Muta la lista aplicando la funcion a cada elemento.
    '''
    for i in range(len(lista)):
        lista[i] = funcion(lista[i])
        
def sumaMil(x):
    return x + 1000
        
L = [3.2, -15, 12.6]

aplicar_a_cada_elemento(L, abs)
print(L)

aplicar_a_cada_elemento(L, int)
print(L)

aplicar_a_cada_elemento(L, sumaMil)
print(L)

