
# IN: str
nombre = input("Introduzca su nombre: ")
print("Hola,", nombre)

# input siempre genera strings
x = input("Introduzca un numero (x): ")
y = input("Introduzca un numero (y): ")
print("SIN conversion) x + y es:", x+y)

# Necesitamos convertilos a números con int()!
x = int(x)
y = int(y)
print("CON conversion) x + y es:", x+y)