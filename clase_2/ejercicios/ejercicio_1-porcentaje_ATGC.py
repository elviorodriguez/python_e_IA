# -*- coding: utf-8 -*-
# Escribir un programa que:
#   - Tome como input una secuencia de nucleótidos
#   - Calcule el porcentaje de A, T, G y C


# ------ TIPS ------
# # Iterar letra a letra
# for letra in 'palabra':
#   print(letra)

# ------ SOLO USAR ------
#  - Ramificacion	(if, elif, else)
#  - Operaciones    (+, -, *, /, etc.)
#  - Comparaciones	(==, !=, <=, >, etc.)
#  - Logica         (and, or, not)
#  - Iteración		(for, while, break)
 
# ------ RECOMENDACIONES ------
# 1ero)	Iterar sobre la secuencia e identificar que nt está en cada posición: preocuparse de 
#       contar después. Combinar también con ramificación (if, elif, else). 
# 2do) 	Contar los nt a medida que se itera.
# 3ro)	Con los valores finales, calcular el %.

###############################################################################
# ------------------- Escribir la solucion al problema aca ------------------ #
###############################################################################

# INPUT
secuencia = 'ATCGGCTAAGCTTAGCGATCGGCTAAGCTT'

# CÓDIGO ACÁ <---------


###############################################################################
# ------------------- Dataset de prueba para copiar y pegar ----------------- #
###############################################################################
# Si anda con todos estos ejemplos, entonces, el programa funciona

# Esperado: A = 100, T: 0, C: 0, G: 0
secuencia = 'AAAAA'

# Esperado: A = 100, T: 0, C: 0, G: 0
secuencia = 'A'

# Esperado: A = 0, T: 100, C: 0, G: 0
secuencia = 'TTTTT'

# Esperado: A = 0, T: 100, C: 0, G: 0
secuencia = 'T'

# Esperado: A = 0, T: 0, C: 100, G: 0
secuencia = 'CCCCC'

# Esperado: A = 0, T: 0, C: 100, G: 0
secuencia = 'C'

# Esperado: A = 0, T: 0, C: 0, G: 100
secuencia = 'GGGGG'

# Esperado: A = 0, T: 0, C: 0, G: 100
secuencia = 'G'

# Esperado: A = 0, T: 0, C: 0, G: 0
secuencia = ''

# Esperado: A = 25, T: 25, C: 25, G: 25
secuencia = 'ATCG'

# Esperado: A = 50, T: 0, C: 0, G: 50
secuencia = 'GAGAGA'