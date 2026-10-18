# -*- coding: utf-8 -*-

# INPUT
N0 = 1000       # Células iniciales
Nf = 10000000   # Células finales
t_dup = 2


# CODIGO AQUÍ


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
    
