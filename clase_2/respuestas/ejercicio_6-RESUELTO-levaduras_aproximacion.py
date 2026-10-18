# -*- coding: utf-8 -*-

# INPUT
N0 = 1000       # Células iniciales
Nf = 10000000   # Células finales
t_dup = 2

# variables para guardar el resultado
t = 0
N = N0
delta = 0.01
epsilon = 10000

# Verificamos si alcanzamos la población final
while abs(Nf - N) > epsilon and N < Nf:
    
    # Subimos una generación
    t += delta
    
    # Duplicamos la población
    N = N0 * 2**(t/t_dup)

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
    
