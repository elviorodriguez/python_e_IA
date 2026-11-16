# -*- coding: utf-8 -*-
import numpy as np

OD600 = np.array([0.12, 0.25, 0.48, 0.91, 1.60, 1.85, 0.05])

# Comparar un array devuelve un array de True/False ---------------------------
mascara = OD600 > 0.5
print(mascara)

# Usamos la máscara para FILTRAR ----------------------------------------------
print(OD600[mascara])           # solo los valores > 0.5
print(OD600[OD600 > 0.5])       # forma abreviada

# Contar cuántos cumplen la condición (True = 1, False = 0) -------------------
print("Cuántos > 0.5:", mascara.sum())
print("Proporción   :", mascara.mean())

# Combinar condiciones: & (and) | (or) ~ (not) --------------------------------
# OJO: cada condición va entre paréntesis y NO se usan and/or/not
fase_log = (OD600 > 0.2) & (OD600 < 1.0)
print(OD600[fase_log])

fuera_de_rango = (OD600 < 0.1) | (OD600 > 1.8)
print(OD600[fuera_de_rango])

# np.where: elegir un valor u otro según una condición ------------------------
etiquetas = np.where(OD600 > 0.5, "denso", "diluido")
print(etiquetas)

# Reemplazar valores usando una máscara ---------------------------------------
corregido = OD600.copy()
corregido[corregido < 0.1] = 0.1     # piso mínimo de 0.1
print(corregido)
