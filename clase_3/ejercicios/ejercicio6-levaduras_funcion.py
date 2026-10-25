# -*- coding: utf-8 -*-

# Reescribir el programa de levaduras para que se ejecute:
# - Como una función que tome como argumento los valores de 𝑇_𝑑, 𝑁_0 y 𝑁_𝑓.
# - Que calcule el tiempo necesario para alcanzar  distintos valoer de 𝑁_𝑓
#   a partir de distintos 𝑁_0 y 𝑇_𝑑 utilizando el algoritmo de búsqueda por
#   bisección.

###############################################################################
# -------------------- REESCRIBIR EL CÓDIGO COMO FUNCIÓN -------------------- #
###############################################################################

# INPUT
N0 = 1000       # Células iniciales
Nf = 10000000   # Células finales
t_dup = 2

# Variables para generar las adivinaciones y el resultado
t_min = 0
t_max = 200
t = (t_min + t_max) / 2
N = N0 * 2**(t/t_dup)

epsilon = 10000

# Verificamos si alcanzamos la población final
while abs(Nf - N) > epsilon:
        
    if N < Nf:
        t_min = t
    else:
        t_max = t 
    
    # Recalculamos la población con un nuevo valor de t
    t = (t_min + t_max) / 2
    N = N0 * 2**(t/t_dup)
    
