# -*- coding: utf-8 -*-
import numpy as np

# Indexado 1D (igual que en listas y str) -------------------------------------
OD600 = np.array([0.12, 0.25, 0.48, 0.91, 1.60, 1.85])

print(OD600[0])        # primer elemento
print(OD600[-1])       # último elemento
print(OD600[1:4])      # slicing [start:end] (end NO incluido)
print(OD600[::2])      # slicing con paso

# Indexado 2D: matriz[fila, columna] -----------------------------------------
# Filas = muestras | Columnas = genes
expresion = np.array([[5.1, 2.0, 8.3, 1.2],
                      [4.8, 2.2, 7.9, 1.0],
                      [9.7, 0.9, 3.1, 4.4]])

print(expresion[1, 2])       # fila 1, columna 2 -> 7.9
print(expresion[0, :])       # fila 0 completa
print(expresion[:, 0])       # columna 0 completa
print(expresion[0:2, 1:3])   # submatriz (filas 0-1, columnas 1-2)

# CUIDADO: un slice es una VISTA (no una copia) -------------------------------
vista = OD600[0:3]
vista[0] = 999
print(OD600)                 # ¡El original también cambió!

# Si queremos una copia independiente usamos .copy() --------------------------
OD600 = np.array([0.12, 0.25, 0.48, 0.91, 1.60, 1.85])
copia = OD600[0:3].copy()
copia[0] = 999
print(OD600)                 # El original NO cambió
