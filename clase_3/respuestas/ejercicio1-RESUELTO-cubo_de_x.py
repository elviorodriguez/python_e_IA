# -*- coding: utf-8 -*-

# INPUT
x = int(input("Ingrese un número entero: "))

# variable para guardar el resultado
resultado = 0

# x + x + ... + x (x veces)
for i in range(abs(x)):
    # (x + x + ... + x) * x (x * x veces)
    for j in range(abs(x)):
        resultado = resultado + x
        
        # Progreso
        print('i =', str(i), '|', 'j =', str(j), '| resultado =', resultado)

# OUTPUT
print('Resultado final: (x**3) =', resultado)
print('Resultado esperado: (control) =', x**3)
print('¿Está bien?:', resultado == x**3)

