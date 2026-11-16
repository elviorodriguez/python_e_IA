# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Create a sample 2D array
data = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

plt.imshow(data, cmap='viridis')
plt.colorbar(label='Valor')
plt.title('Visualizacion de Array 2D')
plt.xlabel('Columnas')
plt.ylabel('Filas')

# ---------------- Agregar nombres a las filas y las columnas -----------------

# Nombres de columnas y filas
columnas = ["A", "B", "C", "D"]
filas = ["Muestra1", "Muestra2", "Muestra3", "Muestra4"]

# Etiquetas de ejes
plt.xticks(range(len(columnas)), columnas)
plt.yticks(range(len(filas)), filas)

plt.show()