# -*- coding: utf-8 -*-

# INPUT
N0 = 2          # Células iniciales
Nf = 10000000   # Células finales

# variables para guardar el resultado
gen = 0
N = N0

# Verificamos si alcanzamos la población final
while N < Nf:
    
    # Subimos una generación
    gen += 1
    
    # Duplicamos la población
    N = 2 * N

# OUTPUT
if N != Nf:
    print("NO se alcanzó la población esperada.")
    print("   - Generaciones:", gen)
    print("   - Población esperada (Nf):", Nf)
    print("   - Población alcanzada (N):", N)
else:
    print("Se alcanzó la población esperada!")
    print("   - Generaciones:", gen)
    print("   - Población final (Nf):", Nf)
    print("   - Población alcanzada (N):", N)
