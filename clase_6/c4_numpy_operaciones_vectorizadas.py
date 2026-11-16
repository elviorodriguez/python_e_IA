# -*- coding: utf-8 -*-
import numpy as np

# Las operaciones se aplican elemento a elemento ------------------------------
OD600 = np.array([0.12, 0.25, 0.48, 0.91, 1.60])
blanco = 0.05
dilucion = 1/2

print(OD600 * (1/dilucion) )          # array * escalar
print(OD600 - blanco)                 # restar el blanco a todas las lecturas
print(OD600 ** 2)

# Entre arrays del mismo tamaño -----------------------------------------------
control = np.array([10.0, 12.0, 11.0, 9.0])
tratado = np.array([20.0, 30.0, 11.0, 4.5])
fold_change = tratado / control
print(fold_change)

