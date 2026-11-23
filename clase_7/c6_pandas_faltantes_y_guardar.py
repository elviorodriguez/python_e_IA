# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("datos_levaduras.csv")

# Detectar datos faltantes (NaN) ----------------------------------------------
print(df.isna().sum())                    # cuántos NaN hay por columna
print(df[df["OD600"].isna()])             # filas con OD600 faltante

# Opción 1: eliminar las filas con faltantes ----------------------------------
sin_nan = df.dropna()
print(df.shape, "->", sin_nan.shape)

# Opción 2: eliminar solo si falta una columna concreta -----------------------
sin_nan_OD = df.dropna(subset=["OD600"])

# Opción 3: reemplazar los faltantes (ej: por la media de la columna) ---------
df["proteina_ug_mL"] = df["proteina_ug_mL"].fillna(df["proteina_ug_mL"].mean())
print(df.isna().sum())

# Pandas ignora los NaN en los cálculos (a diferencia de NumPy) ---------------
print(df["OD600"].mean())

# Guardar resultados ----------------------------------------------------------
sin_nan.to_csv("datos_levaduras_limpio.csv", index=False)
# sin_nan.to_excel("datos_levaduras_limpio.xlsx", index=False)   # requiere openpyxl
print("Archivo guardado")
