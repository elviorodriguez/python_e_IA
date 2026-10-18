# -*- coding: utf-8 -*-

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

num_iter = 0

# Verificamos si alcanzamos la población final
while abs(Nf - N) > epsilon:
    
    # Numero de iteraciones:
    print(" Iter.:", num_iter,  "| N:", N, "| F:", abs(Nf - N))
    
    if N < Nf:
        t_min = t
    else:
        t_max = t 
    
    # Recalculamos la población con un nuevo valor de t
    t = (t_min + t_max) / 2
    N = N0 * 2**(t/t_dup)
    
    # Sumamos +1 iteracion para llevar la cuenta
    num_iter += 1    


# OUTPUT
if Nf - N > epsilon:
    print("NO se alcanzó la población esperada.")
    print("   - Tiempo:", t, "h")
    print("   - Población esperada (Nf):", Nf)
    print("   - Población alcanzada (N):", N)
else:
    print("Se alcanzó la población esperada!")
    print("   - Tiempo necesario:", t, "h")
    print("   - Población esperada (Nf):", Nf)
    print("   - Población alcanzada (N):", N)
    
