# -*- coding: utf-8 -*-

x = 0

# Agregamos 0.1 diez veces
for i in range(10):
    x += 0.1
    
if x == 1:
    print(x, "= 1.0")
else:
    print("¡¿Qué?!", x, "en vez de 1.0!!!")

# A partir de cuantos digitos significativos se vuelve False? 
digitos = 10
if round(x, digitos) == round(1.00, digitos):
    print(" - Redondeando con", digitos, "digitos:", x , "== 1.0 --> True")
else:
    print(" - Redondeando con", digitos, "digitos:", x , "== 1.0 --> False")

tolerancia = 10**(-digitos)
if abs(x - 1.00) < tolerancia:
    print(" - Con tolerancia de", digitos, "digitos:", x , "== 1.0 --> True")
else:
    print(" - Con tolerancia de", digitos, "digitos:", x , "== 1.0 --> False")