# -*- coding: utf-8 -*-

# INPUT
x = int(input("Ingrese un número entero >= 0: "))

# variable para guardar el resultado
resultado = 0

# x + x + ... + x (x veces)
for i in range(x):
    resultado = resultado + x
    
    # Progreso
    print('Iteración (i = ' + str(i) + ') | resultado = ' + str(resultado))

# OUTPUT
print('Resultado final: (x**2) =', resultado)
print('Resultado esperado: (control) =', x**2)
print('¿Está bien?:', x**2 == resultado)

