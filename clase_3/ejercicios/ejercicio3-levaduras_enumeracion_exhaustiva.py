# -*- coding: utf-8 -*-

'''
EJERCICIO 3:

Escribir un programa que:
 - Tome como input valores para 𝑁_0 y 𝑁_𝑓
 - Sabiendo que en cada generación se duplica el número de células:
   calcule el número entero (int) de generaciones mínimas necesarias
   para alcanzar 𝑁_𝑓 a partir de 𝑁_0 utilizando un algoritmo de
   enumeración exhaustiva

Recomendaciones:
1ero)	Extrapolar el cálculo de raices a este ejemplo biológico.
2do) 	Pensar cual es la función de decremento (F).

Solo usar:
 - Ramificacion	 (if, elif, else)
 - Operaciones   (+, -, *, /, etc.)
 - Comparaciones (==, !=, <=, >, etc.)
 - Logica        (and, or, not)
 - Iteración	 (for, while, break)
'''

# INPUT (usá estos valores como INPUT: cambialos cuando tengas una solución)
N0 = 2
Nf = 10000000

# Variables para guardar el resultado (usá estos nombres de variables)
generacion = 0
N = N0

# Modificá las variables generacion y N usando un while loop para obtener
# el Nº de generaciones mínimo (Nº entero) para alcanzar Nf

# ------------> ¡¡¡SOLUCIÓN ACÁ!!! <------------ REEMPLAZALO CON TU CÓDIGO
# ------------> ¡¡¡SOLUCIÓN ACÁ!!! <------------ REEMPLAZALO CON TU CÓDIGO
# ------------> ¡¡¡SOLUCIÓN ACÁ!!! <------------ REEMPLAZALO CON TU CÓDIGO


# OUTPUT (usá este código para ver los valores finales de generacion y N)
if N != Nf:
    print("NO se alcanzó la población esperada.")
    print("   - Generaciones:", generacion)
    print("   - Población esperada (Nf):", Nf)
    print("   - Población alcanzada (N):", N)
else:
    print("Se alcanzó la población esperada!")
    print("   - Generaciones:", generacion)
    print("   - Población final (Nf):", Nf)
    print("   - Población alcanzada (N):", N)
