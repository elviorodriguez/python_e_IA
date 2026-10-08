# -*- coding: utf-8 -*-
# Escribir un programa que:
#   - Tome como input una secuencia de nucleotidos
#   - Encuentre el número de repeticiones del motivo TATAAAA (TATA-box)
#   - En caso de no haber TATA-box, debe decirlo

# ------ TIP ------
# # Comparación de strings
# 'AGTTAT' == 'TATAAAA' --> False
# # Indexado
# 'AGTTAT'[2:6] --> 'TTA'



# ------ SOLO USAR ------
#  - Ramificacion	(if, elif, else)
#  - Operaciones    (+, -, *, /, etc.)
#  - Comparaciones	(==, !=, <=, >, etc.)
#  - Logica         (and, or, not)
#  - Iteracion      (for, while, break)

# ------ RECOMENDACIONES ------
# 1ero) Encontrar TATA-box : Resolver cómo recorrer la secuencia e identificar
#       TATA-boxes.
# 2do)  Contar cuantos hay: Resolver como contar a medida que progresa.
# 3ro)  Errores: Es probable que se encuentren 	con IndexError. Pensar en el
#       largo de la secuencia y el largo del TATA-box.

###############################################################################
# ------------------- Escribir la solucion al problema aca ------------------ #
###############################################################################

# INPUT
secuencia = 'ATCGTATAAAAGCTTAGCGTATAAAACTAAGCTT'
motivo = 'TATAAAA'

# Solución aquí


###############################################################################
# ------------------- Dataset de prueba para copiar y pegar ----------------- #
###############################################################################
# Si anda con todos estos ejemplos, entonces, el programa funciona

# Esperado: 0
secuencia = ''

# Esperado: 1
# Secuencia exactamente igual al motivo
secuencia = 'TATAAAA'

# Esperado: 0
secuencia = 'ATCGGCTAGCTG'

# Esperado: 1
secuencia = 'ATCGTATAAAAGCTT'

# Esperado: 2
secuencia = 'TATAAAAGCTTATATAAAAGC'

# Esperado: 1
# Motivo al principio
secuencia = 'TATAAAAGCTTAGCG'

# Esperado: 1
# Motivo al final
secuencia = 'ATCGGCTTAGCTTATAAAA'

# Esperado: 0
# Secuencia más corta que el motivo
secuencia = 'TATAA'

# Esperado: 0
# Secuencia de un solo nucleótido
secuencia = 'A'

# Esperado: 2
# Dos motivos separados
secuencia = 'TATAAAAGCGCGTATAAAA'

# Esperado: 2
# Dos motivos consecutivos
secuencia = 'TATAAAATATAAAA'

# Esperado: 3
# Tres motivos
secuencia = 'ATATAAAAGCTTATATAAAAGGTATAAAAT'

# Esperado: 1
# Motivo muy cerca del principio
secuencia = 'GTATAAAAC'

# Esperado: 1
# Motivo muy cerca del final
secuencia = 'CGTATAAAAG'

# Esperado: 0
# Muchas T y A, pero ninguna coincidencia completa
secuencia = 'TTTTAAAATTTAAAATTT'

# Esperado: 1
# Coincidencia dentro de una secuencia con muchas bases alrededor
secuencia = 'GGGGGGGTATAAAAGGGGGGG'