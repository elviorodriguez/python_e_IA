# -*- coding: utf-8 -*-

# Creando tuples
T_vacio = ()
T_1 = (1, "dos", 3)
T_2 = (T_vacio, T_1, 3.2)

print(T_vacio)
print(T_1)
print(T_2)

# Tuple con un solo elemento
T_unitario_mal  = (1)
T_unitario_bien = (1,)

print(T_unitario_mal)
print(T_unitario_bien)

# Operaciones e indexado (como con strings)
T_1 + T_1
3 * T_1
T_1[0]
T_1[1:3]

# Los tuples son inmutables (esto da un error)
T_1[0] = 0

# Se puede iterar sobre los elementos
for elemento in T_1:
    print("ΕLEMENTO -->", elemento)
    
    