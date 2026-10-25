# -*- coding: utf-8 -*-

# INPUT (Raices perfectas: 1, 4, 9, 16, 25, 36, 49, 64)
x = float(input("Ingrese un Nº real >= 1: "))

# Variables para generar las adivinaciones y el resultado
n = 0
delta = 0.001
epsilon = 0.01

# Para seguir en número de iteraciones
num_iter = 0

# Verificación
while abs(x - n * n) > epsilon:
    
    # Enumeración exhaustiva por adición
    n += delta
    
    # Sumamos +1 iteracion para llevar la cuenta
    num_iter += 1
    
# Función de decremento:
print("   - Nº de iteraciones:", num_iter)

# OUTPUT
if abs(x - n * n) > epsilon:
    print("Fallamos en encontrar el cuadrado de", x)
else:
    print("La raiz cuadrada de", x, "es", n)
