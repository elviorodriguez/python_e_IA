# -*- coding: utf-8 -*-

def raizCuadradaBiseccion(x, epsilon = 0.001):
    
    # Variables para generar las adivinaciones y el resultado
    n_min = 0
    n_max = x
    n = (n_min + n_max) / 2
    
    # Verificación
    while abs(x - n * n) > epsilon and n < x:
                
        if n * n < x:
            n_min = n
        else:
            n_max = n
        
        # Recalculamos
        n = (n_min + n_max) / 2
    
    return n

# Cambiamos facilmente de input o de epsilon
print(raizCuadradaBiseccion(1))
print(raizCuadradaBiseccion(8))
print(raizCuadradaBiseccion(9))
print(raizCuadradaBiseccion(9, epsilon = 0.00001))
print(raizCuadradaBiseccion(9, epsilon = 0.000000000000001))