# -*- coding: utf-8 -*-

# INPUT (Raices perfectas: 1, 4, 9, 16, 25, 36, 49, 64)
x = float(input("Ingrese un Nº > 1: "))

# Variables para generar las adivinaciones y el resultado
n_min = 0
n_max = x
n = (n_min + n_max) / 2
epsilon = 0.001

# Para seguir en número de iteraciones
num_iter = 0

# Verificación
while abs(x - n * n) > epsilon and n < x:
    
    # Numero de iteraciones:
    print(" Iter.:", num_iter,  "| n:", n, "| F:", abs(x - n * n))
    
    if n * n < x:
        n_min = n
    else:
        n_max = n
    
    # Recalculamos
    n = (n_min + n_max) / 2
    
    # Sumamos +1 iteracion para llevar la cuenta
    num_iter += 1    
    
    
# OUTPUT
if abs(x - n * n) > epsilon:
    print("Falló el cálculo del cuadrado de", x)
else:
    print("La raiz cuadrada de", x, "es", n)


