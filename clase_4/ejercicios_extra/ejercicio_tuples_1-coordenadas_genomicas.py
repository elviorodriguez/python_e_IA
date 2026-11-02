# -*- coding: utf-8 -*-

# Escribir un programa que:
#   - Tome como input una lista de exones, donde cada exón es una tuple
#     con su posición de inicio y fin en el genoma: (inicio, fin)
#   - Calcule el largo de cada exón (fin - inicio)
#   - Identifique el exón más largo e imprima su índice, coordenadas y largo
#   - Calcule e imprima el largo total del transcripto (suma de todos los exones)

# ------ TIP ------
# # Las tuples se acceden por índice (igual que las listas) pero NO se modifican
# exon = (1500, 1800)
# exon[0]   --> 1500   (inicio)
# exon[1]   --> 1800   (fin)

# # Lista de tuples
# exones = [(100, 300), (500, 750), (900, 1200)]
# exones[0]        --> (100, 300)
# exones[0][0]     --> 100
# exones[0][1]     --> 300

# ------ SOLO USAR ------
#  - Ramificacion	(if, elif, else)
#  - Operaciones    (+, -, *, /, etc.)
#  - Comparaciones	(==, !=, <=, >, etc.)
#  - Logica         (and, or, not)
#  - Iteración		(for, while, break)
#  - Tuples         (indexado, len)
#  - Listas         (indexado, len, range)

# ------ RECOMENDACIONES ------
# 1ero)  Recorrer la lista de exones con range(len(...)) para tener el índice.
# 2do)   En cada iteración, calcular el largo del exón con fin - inicio.
# 3ro)   Ir recordando cuál es el exón más largo (similar a recordar la G más larga).
# 4to)   Acumular el largo total sumando el largo de cada exón.

###############################################################################
# ------------------- Escribir la solucion al problema aca ------------------ #
###############################################################################

# INPUT: lista de tuples (inicio, fin) en pares de bases — gen BRCA1 simplificado
exones = [
    (100,  250),    # exón 0
    (500,  820),    # exón 1
    (1100, 1180),   # exón 2
    (1500, 2100),   # exón 3
    (2400, 2550),   # exón 4
]

# Variables para guardar resultados
largo_max   = 0
indice_max  = 0
largo_total = 0

# SOLUCIÓN AQUÍ


# OUTPUT
print("Exón más largo:")
print("   - Índice:", indice_max)
print("   - Coordenadas:", exones[indice_max])
print("   - Largo:", largo_max, "pb")
print("Largo total del transcripto:", largo_total, "pb")


###############################################################################
# ------------------- Dataset de prueba para copiar y pegar ----------------- #
###############################################################################
# Si anda con todos estos ejemplos, el programa funciona correctamente

# Esperado: exón más largo = índice 0, largo 500. Total = 500
exones = [(0, 500)]

# Esperado: exón más largo = índice 1 (largo 400). Total = 700
exones = [(0, 300), (500, 900), (1000, 1100)]

# Esperado: exón más largo = índice 0 (largo 600). Total = 1050
exones = [(0, 600), (700, 850), (900, 1050), (1100, 1250)]

# Esperado: todos tienen largo 100. El más largo es el índice 0. Total = 300
exones = [(0, 100), (200, 300), (400, 500)]
