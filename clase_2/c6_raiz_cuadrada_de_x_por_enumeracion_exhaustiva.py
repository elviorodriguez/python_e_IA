# -*- coding: utf-8 -*-

# INPUT (Raices perfectas: 1, 4, 9, 16, 25)
x = int(input("Ingrese un Nº entero >= 0: "))

# Variable para generar las adivinaciones y el resultado
n = 0

# Verificación
while n * n < x:
    
    # Enumeración exhaustiva por adición
    n += 1

# OUTPUT
if n * n != x:
    print(x, "no es un cuadrado perfecto.")
else:
    print("La raiz cuadrada de", x, "es", n)
   