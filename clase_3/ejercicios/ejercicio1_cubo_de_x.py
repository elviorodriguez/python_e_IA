# -*- coding: utf-8 -*-

# Reescribir el programa x^2 para que:
#   - Tome como input cualquier −∞ < entero < +∞
#   - Calcule x^3 y lo imprima

# ------ TIPS ------

# # Bucles adentro de bucles
# for i in range(x):
# 	for j in range(x):
# 		print(i, j)

# # Valores absolutos
# abs(-3) --> 3

# ------ SOLO USAR ------

#  - Ramificacion	(if, elif, else)
#  - Operaciones    (+, -, *, /, etc.)
#  - Comparaciones	(==, !=, <=, >, etc.)
#  - Logica         (and, or, not)
#  - Iteración		(for, while, break)

###############################################################################
# ------------- MODIFICAR EL CÓDIGO DE x**2 para computar x**3 -------------- #
###############################################################################

# INPUT 
x = int(input("Ingrese un número entero >= 0: "))

# variable para guardar el resultado
resultado = 0

for i in range(x):
    resultado = resultado + x
    print('Iteración (i = ' + str(i) + ') | resultado = ' + str(resultado))

# OUTPUT
print('Resultado final: (x**2) =', resultado)
print('Resultado esperado: (control) =', x**2)
print('¿Está bien?:', x**2 == resultado)
