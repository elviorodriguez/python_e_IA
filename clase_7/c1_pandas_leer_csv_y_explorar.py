# -*- coding: utf-8 -*-
import pandas as pd

# OJO: el archivo .csv tiene que estar en la carpeta de trabajo (working dir)
# o hay que indicar la ruta completa.

# Leer un archivo CSV ---------------------------------------------------------
df = pd.read_csv("datos_levaduras.csv", sep = ",")

# Primer vistazo a los datos --------------------------------------------------
print(df.head())           # primeras 5 filas
print(df.tail(3))          # últimas 3 filas
print(df.shape)            # (filas, columnas)
print(df.columns.tolist()) # lista con los nombres de las columnas

# Tipos de datos y valores no nulos por columna -------------------------------
df.info()

# Resumen estadístico de las columnas numéricas -------------------------------
print(df.describe())

# Contar categorías de una columna --------------------------------------------
print(df["cepa"].value_counts())
print(df["cepa"].unique())
print(df["condicion"].value_counts())
print(df["condicion"].unique())

# Otros formatos de entrada ---------------------------------------------------
# df = pd.read_csv("datos.tsv", sep="\t")     # separado por tabulaciones
# df = pd.read_excel("datos.xlsx")            # Excel (requiere openpyxl)
