# -*- coding: utf-8 -*-

# Escribir un programa que:
#  - Tome como input valores para 𝑁_0 y 𝑁_𝑓
#  - Sabiendo que en cada generación se duplica el número
#    de células: calcule el número de generaciones necesarias para
#    alcanzar 𝑁_𝑓 a partir de 𝑁_0 utilizando un algoritmo de
#    enumeración exhaustiva


# ------ RECOMENDACIONES ------
# 1ero)	Extrapolar el cálculo de raices a este ejemplo biológico.
# 2do) 	Pensar cual es la función de decremento (F).

# ------ SOLO USAR ------

#  - Ramificacion	(if, elif, else)
#  - Operaciones    (+, -, *, /, etc.)
#  - Comparaciones	(==, !=, <=, >, etc.)
#  - Logica         (and, or, not)
#  - Iteración		(for, while, break)

# INPUT
N0 = 2
Nf = 10000000

# variables para guardar el resultado
gen = 0
N = N0

# SOLUCIÓN AQUÍ


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
