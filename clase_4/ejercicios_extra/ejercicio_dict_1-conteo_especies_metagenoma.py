# -*- coding: utf-8 -*-

# Escribir un programa que:
#   - Tome como input una lista de lecturas de metagenómica, donde cada lectura
#     fue asignada a una especie (string con el nombre de la especie)
#   - Use un diccionario para contar cuántas lecturas corresponden a cada especie
#   - Imprima cada especie con su conteo y su abundancia relativa (%)
#   - Identifique e imprima la especie más abundante

# ------ TIP ------
# # Diccionarios: crear, agregar y actualizar claves
# conteo = {}                     # diccionario vacío
# conteo['E. coli'] = 1           # crear clave nueva con valor 1
# conteo['E. coli'] = conteo['E. coli'] + 1   # incrementar valor existente

# # Verificar si una clave ya existe antes de acceder
# if 'E. coli' in conteo:
#     conteo['E. coli'] = conteo['E. coli'] + 1
# else:
#     conteo['E. coli'] = 1

# # Iterar sobre un diccionario
# for especie in conteo:
#     print(especie, conteo[especie])

# ------ SOLO USAR ------
#  - Ramificacion	(if, elif, else)
#  - Operaciones    (+, -, *, /, etc.)
#  - Comparaciones	(==, !=, <=, >, etc.)
#  - Logica         (and, or, not)
#  - Iteración		(for, while, break)
#  - Diccionarios   (crear, acceso por clave, operador in, iterar)
#  - Listas         (len, indexado)

# ------ RECOMENDACIONES ------
# 1ero)  Recorrer la lista de lecturas una por una.
# 2do)   Para cada lectura, verificar si la especie ya está en el diccionario.
#        Si está → incrementar el conteo. Si no está → agregar con conteo = 1.
# 3ro)   Calcular el total de lecturas (len de la lista original).
# 4to)   Recorrer el diccionario para imprimir cada especie, su conteo y su %.
# 5to)   En el mismo recorrido (o en uno separado), identificar la especie más abundante.

###############################################################################
# ------------------- Escribir la solucion al problema aca ------------------ #
###############################################################################

# INPUT: cada elemento es la especie asignada a una lectura de secuenciación
lecturas = [
    'E. coli', 'Salmonella sp.', 'E. coli', 'Lactobacillus sp.',
    'E. coli', 'Salmonella sp.', 'Bacteroides sp.', 'E. coli',
    'Lactobacillus sp.', 'E. coli', 'Bacteroides sp.', 'E. coli',
    'Salmonella sp.', 'Lactobacillus sp.', 'E. coli', 'Bacteroides sp.',
]

# Variables para guardar resultados
conteo_especies  = {}   # diccionario vacío para contar
especie_max      = ''
conteo_max       = 0

# SOLUCIÓN AQUÍ


# OUTPUT
total = len(lecturas)
print("Abundancia de especies en la muestra:")
print("-" * 40)
for especie in conteo_especies:
    abundancia = conteo_especies[especie] / total * 100
    print(especie, ":", conteo_especies[especie], "lecturas (", abundancia, "%)")

print("-" * 40)
print("Especie más abundante:", especie_max, "con", conteo_max, "lecturas")


###############################################################################
# ------------------- Dataset de prueba para copiar y pegar ----------------- #
###############################################################################
# Si anda con todos estos ejemplos, el programa funciona correctamente

# Esperado: E. coli = 100%
lecturas = ['E. coli', 'E. coli', 'E. coli']

# Esperado: A=1(50%), B=1(50%). Más abundante: A (o B, ambos con 1)
lecturas = ['A', 'B']

# Esperado: E. coli=3, Salmonella=2, Lactobacillus=1. Más abundante: E. coli
lecturas = ['E. coli', 'Salmonella sp.', 'E. coli', 'Lactobacillus sp.',
            'E. coli', 'Salmonella sp.']

# Esperado: una sola especie con 100%
lecturas = ['Bacteroides sp.']

# Esperado: 4 especies distintas, cada una con 25%
lecturas = ['E. coli', 'Salmonella sp.', 'Lactobacillus sp.', 'Bacteroides sp.']
