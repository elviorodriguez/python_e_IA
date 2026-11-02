# -*- coding: utf-8 -*-

# Escribir un programa que:
#   - Tome como input una lista de genes con sus longitudes (en pares de bases)
#   - Filtre los genes que superen un umbral de longitud mínima dado
#   - Imprima los genes que pasaron el filtro y cuántos son

# ------ TIP ------
# # Listas y sus operaciones básicas
# genes = ['geneA', 'geneB', 'geneC']
# genes[0]          --> 'geneA'
# len(genes)        --> 3
# genes.append('geneD')   # agrega al final

# # Iterar sobre dos listas en paralelo con range + len
# for i in range(len(lista)):
#     print(lista_nombres[i], lista_valores[i])

# ------ SOLO USAR ------
#  - Ramificacion	(if, elif, else)
#  - Operaciones    (+, -, *, /, etc.)
#  - Comparaciones	(==, !=, <=, >, etc.)
#  - Logica         (and, or, not)
#  - Iteración		(for, while, break)
#  - Listas         (list, append, len, indexado)

# ------ RECOMENDACIONES ------
# 1ero)  Recorrer ambas listas en paralelo (nombres y longitudes).
# 2do)   En cada iteración, preguntar si la longitud supera el umbral.
# 3ro)   Si supera el umbral, guardar el nombre en una nueva lista de resultados.
# 4to)   Al final, imprimir cuántos genes pasaron el filtro y cuáles son.

###############################################################################
# ------------------- Escribir la solucion al problema aca ------------------ #
###############################################################################

# INPUT
nombres_genes  = ['BRCA1', 'TP53', 'MYC', 'EGFR', 'PTEN', 'ALK', 'KRAS']
longitudes_pb  = [81189,   19149,  5161,  188307, 87892,  728787, 45000 ]
umbral_min     = 50000   # pares de bases

# Variables para guardar el resultado
genes_filtrados = []

# SOLUCIÓN AQUÍ


# OUTPUT
if len(genes_filtrados) == 0:
    print("Ningún gen supera el umbral de", umbral_min, "pb.")
else:
    print("Genes que superan", umbral_min, "pb:", len(genes_filtrados))
    for gen in genes_filtrados:
        print("  -", gen)


###############################################################################
# ------------------- Dataset de prueba para copiar y pegar ----------------- #
###############################################################################
# Si anda con todos estos ejemplos, el programa funciona correctamente

# Esperado: BRCA1, EGFR, PTEN, ALK
nombres_genes = ['BRCA1', 'TP53', 'MYC', 'EGFR', 'PTEN', 'ALK', 'KRAS']
longitudes_pb = [81189,   19149,  5161,  188307, 87892,  728787, 45000 ]
umbral_min    = 50000

# Esperado: Ningún gen supera el umbral
nombres_genes = ['TP53', 'MYC', 'KRAS']
longitudes_pb = [19149,  5161,  45000 ]
umbral_min    = 100000

# Esperado: todos los genes (3 de 3)
nombres_genes = ['BRCA1', 'EGFR', 'ALK']
longitudes_pb = [81189,   188307, 728787]
umbral_min    = 0

# Esperado: 1 gen (ALK)
nombres_genes = ['BRCA1', 'EGFR', 'ALK']
longitudes_pb = [81189,   188307, 728787]
umbral_min    = 500000
