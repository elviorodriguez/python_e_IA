# -*- coding: utf-8 -*-

# Importar NumPy (por convención se usa el alias np) --------------------------
import numpy as np


# Crear un array a partir de una lista ----------------------------------------
OD600 = np.array([0.12, 0.25, 0.48, 0.91, 1.60])
print(OD600)
print(type(OD600))       # numpy.ndarray

# Crear una matriz a partir de una lista de listas ----------------------------
matriz = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(matriz)

# Crear arrays con funciones --------------------------------------------------
ceros = np.zeros(5)                 # 5 ceros
unos = np.ones((2, 3))              # matriz de 2 filas x 3 columnas
pares = np.arange(0, 10, 2)         # como range(), pero devuelve un array
tiempos = np.linspace(0, 24, 5)     # 5 valores equiespaciados entre 0 y 24 h
print(ceros, unos, pares, tiempos, sep="\n")

# Números aleatorios (con semilla para que sea reproducible) ------------------
rng = np.random.default_rng(seed=1)
ruido = rng.normal(loc=0, scale=1, size=5)   # distribución normal
print(ruido)

# Atributos de un array -------------------------------------------------------
print(matriz.shape)    # (2, 3)  -> (filas, columnas)
print(matriz.ndim)     # 2       -> número de dimensiones
print(matriz.size)     # 6       -> número total de elementos
print(matriz.dtype)    # int64   -> tipo de los elementos

# Todos los elementos son del MISMO tipo (dtype) ------------------------------
mezcla_16 = np.array([1, 2.5, 3], dtype= np.float16)
mezcla_32 = np.array([1, 2.5, 3], dtype= np.float32)
mezcla_64 = np.array([1, 2.5, 3], dtype= np.float64)    # <-- Por defecto 64
enteros = mezcla_16.astype(int)       # conversión explícita
print(enteros)
