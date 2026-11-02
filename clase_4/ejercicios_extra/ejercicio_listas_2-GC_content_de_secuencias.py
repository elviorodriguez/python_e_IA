# -*- coding: utf-8 -*-

# Escribir un programa que:
#   - Tome como input una lista de secuencias de ADN
#   - Calcule el GC content (%) de cada una
#   - Guarde los resultados en una nueva lista
#   - Imprima cada secuencia con su GC content
#   - Al final, imprima el promedio de GC content de todas las secuencias

# ------ TIP ------
# # Listas y sus operaciones básicas
# resultados = []
# resultados.append(42.5)   # agrega un valor al final

# # Iterar con índice
# for i in range(len(lista)):
#     print(i, lista[i])

# # GC content = (G + C) / largo_total * 100
# # Podés reutilizar la lógica del ejercicio de porcentaje ATGC

# ------ SOLO USAR ------
#  - Ramificacion	(if, elif, else)
#  - Operaciones    (+, -, *, /, etc.)
#  - Comparaciones	(==, !=, <=, >, etc.)
#  - Logica         (and, or, not)
#  - Iteración		(for, while, break)
#  - Listas         (list, append, len, indexado)

# ------ RECOMENDACIONES ------
# 1ero)  Para cada secuencia en la lista, contar G y C (reusar lo del ej. de ATGC).
# 2do)   Calcular el GC content de esa secuencia y guardarlo en una nueva lista.
# 3ro)   Al final, recorrer la lista de resultados para calcular el promedio.
# 4to)   Tener en cuenta el caso de una secuencia vacía (largo == 0).

###############################################################################
# ------------------- Escribir la solucion al problema aca ------------------ #
###############################################################################

# INPUT
secuencias = [
    'ATGCGATACGCTTCGAT',
    'GGGCCCGGGCCC',
    'ATATATATAT',
    'GCGCGCGCGCGC',
    'ATTTTTTTTTA',
]

# Variables para guardar resultados
gc_contents = []

# SOLUCIÓN AQUÍ


# OUTPUT
print("Secuencia | GC content (%)")
print("-" * 35)
for i in range(len(secuencias)):
    print(secuencias[i], "|", gc_contents[i])

# PROMEDIO
# CALCULAR E IMPRIMIR ACÁ


###############################################################################
# ------------------- Dataset de prueba para copiar y pegar ----------------- #
###############################################################################
# Si anda con todos estos ejemplos, el programa funciona correctamente

# Esperado: GC = 100.0%
secuencias = ['GCGCGC']

# Esperado: GC = 0.0%
secuencias = ['ATATATATAT']

# Esperado: GC = 50.0%
secuencias = ['ATGC']

# Esperado: promedio = 50.0  (GC de cada una: 100, 0, 50)
secuencias = ['GCGC', 'ATAT', 'ATGC']

# Esperado: secuencia vacía → GC = 0.0 (o indicar que está vacía)
secuencias = ['ATGC', '', 'GCGC']
