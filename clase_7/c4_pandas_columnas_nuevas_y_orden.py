# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

df = pd.read_csv("datos_levaduras.csv")

# Crear una columna nueva (operación vectorizada, sin for) --------------------
df["proteina_por_OD"] = df["proteina_ug_mL"] / df["OD600"]
print(df[["muestra", "OD600", "proteina_ug_mL", "proteina_por_OD"]].head())

# Podemos usar funciones de NumPy sobre columnas ------------------------------
df["log2_expresion"] = np.log2(df["expresion_relativa"])
print(df[["muestra", "expresion_relativa", "log2_expresion"]].head())

# Columna nueva a partir de una condición -------------------------------------
df["fase"] = np.where(df["OD600"] > 1.0, "estacionaria", "exponencial")
print(df["fase"].value_counts())

# Ordenar ---------------------------------------------------------------------
print(df.sort_values("OD600").head())
print(df.sort_values("OD600", ascending=False).head())
print(df.sort_values(["cepa", "OD600"], ascending=[True, False]).head(8))

# Renombrar y eliminar columnas -----------------------------------------------
df = df.rename(columns={"proteina_ug_mL": "proteina"})
df = df.drop(columns=["proteina_por_OD"])
print(df.columns.tolist())
