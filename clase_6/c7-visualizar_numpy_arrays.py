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
plt.xlabel('Indice de Columna')
plt.ylabel('Indice de Fila')
plt.show()

