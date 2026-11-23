# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("datos_levaduras.csv")

# Seleccionar columnas --------------------------------------------------------
print(df["OD600"])                          # una columna -> Serie
print(df[["cepa", "OD600"]])                # varias columnas -> DataFrame

# Seleccionar filas por POSICIÓN con iloc (igual que indexado de NumPy) -------
print(df.iloc[0])                           # primera fila
print(df.iloc[0:3])                         # filas 0, 1 y 2
print(df.iloc[0:3, 1:3])                    # filas 0-2, columnas 1-2

# Seleccionar por ETIQUETA con loc --------------------------------------------
print(df.loc[2, "OD600"])                   # fila con índice 2, columna OD600
print(df.loc[0:3, ["cepa", "OD600"]])       # OJO: en loc el final SÍ se incluye

# Filtrar filas con condiciones (máscaras booleanas, como en NumPy) -----------
alta_OD = df[df["OD600"] > 1.0]
print(alta_OD)

solo_WT = df[df["cepa"] == "WT"]
print(solo_WT)

# Combinar condiciones: & | ~ con paréntesis ----------------------------------
mutantes_calor = df[(df["cepa"] != "WT") & (df["condicion"] == "calor")]
print(mutantes_calor)

# isin: pertenece a una lista de valores --------------------------------------
print(df[df["cepa"].isin(["mutA", "mutB"])])

# Filtrar y quedarnos con ciertas columnas ------------------------------------
print(df.loc[df["expresion_relativa"] > 2, ["muestra", "cepa", "expresion_relativa"]])
