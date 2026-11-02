# -*- coding: utf-8 -*-

# Creando listas
L_vacia = []
L_1 = [1, "dos", 3]
L_2 = [L_vacia, L_1, 3.2]

print(L_vacia)
print(L_1)
print(L_2)

# Lista con un solo elemento (en este caso es lo mismo)
L_unitaria_OK_1 = [1]
L_unitaria_OK_2 = [1,]

print(L_unitaria_OK_1)
print(L_unitaria_OK_2)

# Operaciones e indexado (como con strings)
L_1 + L_1
3 * L_1
L_1[0]
L_1[1:3]

# Las listas son MUTABLES (esto cambia el elemento)
print(L_1)
L_1[0] = "CERO"
print(L_1)

# Se puede iterar sobre los elementos
for elemento in L_1:
    print("ΕLEMENTO -->", elemento)
    
    