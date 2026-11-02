# -*- coding: utf-8 -*-

def min_y_max(tuple_numerico):
    '''
    Toma como input un tuple de números (int o float) y encuentra el minimo y
    el máximo. Devuelve un tuple con el mínimo y el máximo (min, max)
    
    Parameters
    ----------
    tuple_numerico : tuple( int | float )
        tuple compuesto con elementos numéricos (int o float).

    Returns
    -------
    (minVal, maxVal) : tuple( int | float )
        tuple con los valores minimos y máximos del tuple_numerico.

    '''
    minVal = 0
    maxVal = 0
    for numero in tuple_numerico:
        if numero < minVal:
            minVal = numero
        if numero > maxVal:
            maxVal = numero
    
    return (minVal, maxVal)

tuple_numerico = (1000, 1, 2, -201.2, 4, 12)
minVal, maxVal = min_y_max(tuple_numerico)

print("Valor mínimo:", minVal)
print("Valor máximo:", maxVal)

