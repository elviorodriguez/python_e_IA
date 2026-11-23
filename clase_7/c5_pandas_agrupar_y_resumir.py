# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("datos_levaduras.csv")

# groupby: separar -> aplicar una función -> combinar -------------------------
print(df.groupby("cepa")["OD600"].mean())

# Agrupar por más de una columna ----------------------------------------------
print(df.groupby(["cepa", "condicion"])["OD600"].mean())

# Varias estadísticas a la vez con agg ----------------------------------------
resumen = df.groupby(["cepa", "condicion"])["OD600"].agg(["mean", "std", "count"])
print(resumen.round(2))

# Estadísticas distintas para columnas distintas ------------------------------
resumen2 = df.groupby("cepa").agg(
    OD_media=("OD600", "mean"),
    expresion_max=("expresion_relativa", "max"),
    n=("muestra", "count"),
)
print(resumen2.round(2))

# Volver el índice a columnas normales ----------------------------------------
print(resumen.reset_index().round(2))

# Tabla cruzada (cepas en filas, condiciones en columnas) ---------------------
tabla = df.pivot_table(values="OD600", index="cepa", columns="condicion",
                       aggfunc="mean")
print(tabla.round(2))
