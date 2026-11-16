# -*- coding: utf-8 -*-
import numpy as np

# Expresión de 3 genes en 4 muestras ------------------------------------------
# Filas = muestras (4) | Columnas = genes (3)
expresion = np.array([[5.1, 2.0, 8.3],
                      [4.8, 2.2, 7.9],
                      [9.7, 0.9, 3.1],
                      [9.2, 1.1, 3.5]])

# Estadística sobre TODO el array ---------------------------------------------
print("Media total  :", expresion.mean())
print("Desvío total :", expresion.std())
print("Mínimo       :", expresion.min())
print("Máximo       :", expresion.max())
print("Suma         :", expresion.sum())

# axis=0 -> opera "hacia abajo" (colapsa las filas): un valor POR COLUMNA -----
media_por_gen = expresion.mean(axis=0)
print("Media por gen    :", media_por_gen)         # 3 valores

# axis=1 -> opera "hacia el costado" (colapsa las columnas): un valor POR FILA
media_por_muestra = expresion.mean(axis=1)
print("Media por muestra:", media_por_muestra)     # 4 valores

# Posición del máximo ---------------------------------------------------------
print("Gen más expresado (en cada muestra):", expresion.argmax(axis=1))

# Otras funciones útiles ------------------------------------------------------
print(np.median(expresion, axis=0))
print(np.std(expresion, axis=0))
print(np.round(expresion.mean(axis=0), 1))
