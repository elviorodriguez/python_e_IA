# Escribir un programa que:
#   - Examine tres variables numericas (x, y, z)
#   - Imprima el Nº impar mas grande de ellos
#   - Si ninguno es impar, debe indicarlo

# ------ TIPS ------
# # True si es par
# x % 2 == 0
# # True si es impar
# x % 2 != 0

# ------ SOLO USAR ------
#  - Ramificacion	(if, elif, else)
#  - Operaciones    (+, -, *, /, etc.)
#  - Comparaciones	(==, !=, <=, >, etc.)
#  - Logica         (and, or, not)

# ------ RECOMENDACIONES ------
# 1ero)	Identificar los impares: imprimir cada 	número impar, sin intentar
#       encontrar 	todavía el mayor.
# 2do) 	Encontrar el mayor entre tres números: 	practicar comparaciones sin
#       considerar 	la paridad.
# 3ro)	Combinar ambas ideas: encontrar el 	mayor número que cumpla la
#       condición 	de ser impar.

# IN sugeridos:	        OUT esperados:
# x= 1|y= 2|z=-3		1
# x= 2|y= 4|z= 6		Ninguno es impar
# x=10|y= 7|z= 3		7
# x=-1|y=-3|z=-5		-1
# x= 2|y=-7|z= 4		-7
# x= 5|y= 5|z= 3		5
# x= 0|y=-3|z=-2		-3
# x=-4|y=-2|z=-6		Ninguno es impar

# INPUT
x = 1
y = 2
z = -3

# Verificamos si "x" es impar y si es el mayor de los impares
if x % 2 != 0 and (y % 2 == 0 or x >= y) and (z % 2 == 0 or x >= z):
    print(x)

# Verificamos si "y" es impar y si es el mayor de los impares
elif y % 2 != 0 and (x % 2 == 0 or y >= x) and (z % 2 == 0 or y >= z):
    print(y)

# Verificamos si "z" es impar
elif z % 2 != 0:
    
    # La única manera de llegar acá es que z es el único impar: se elije z
    print(z)
        
# Si ninguno de los anteriores fue True, significa que no hay impares
else:
    print("Ninguno es impar")
    