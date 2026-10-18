# -*- coding: utf-8 -*-

# Escribir un programa que:
#   - Tome como input una secuencia de nucleótidos
#   - Encuentre la repetición de G sucesivas más larga
#   - En caso de no haber G, debe decirlo

# ------ TIP ------
# # Iterar letra a letra
# for letra in 'palabra':
#   print(letra)


# ------ SOLO USAR ------
#  - Ramificacion	(if, elif, else)
#  - Operaciones    (+, -, *, /, etc.)
#  - Comparaciones	(==, !=, <=, >, etc.)
#  - Logica         (and, or, not)
#  - Iteración      (for, while, break)

# ------ RECOMENDACIONES ------
# 1ero)	Contar G consecutivos: Resolver como recorrer la secuencia y saber
#       cuantos G consecutivos llevo
# 2do) 	Recordar G mas larga: Mientras se recorre la secuencia preguntarse
#       �como recordar cual fue la corrida mas larga  encontrada hasta ahora?


###############################################################################
# ------------------- Escribir la solucion al problema aca ------------------ #
###############################################################################

# INPUT
secuencia = 'ATCGGCTAAGCTTAGCGATCGGCTAAGCTT'

for nt in secuencia:
    print(nt)
    
    


###############################################################################
# ------------------- Dataset de prueba para copiar y pegar ----------------- #
###############################################################################
# Si anda con todos estos ejemplos, entonces, el programa funciona

# Esperado: 5
secuencia = 'ATCGGGGG'

# Esperado: No hay G
secuencia = ''

# No hay G
secuencia = 'AAAA'

# Esperado: 1
secuencia = 'G'

# Esperado: 3
secuencia = 'GGG'

# Esperado: 2
secuencia = 'ATCGG'

# Esperado: 2
secuencia = 'GGAT'

# Esperado: 3
secuencia = 'GGATGGG'

# Esperado: 1
secuencia = 'GAGAGAG'
