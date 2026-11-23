# -*- coding: utf-8 -*-

# Importar pandas (por convención se usa el alias pd) -------------------------
import pandas as pd

# Series: un array de NumPy con ETIQUETAS (índice) ----------------------------
OD600 = pd.Series([0.12, 0.48, 0.91, 1.60],
                  index=["t0", "t2", "t4", "t6"])
print(OD600)
print(OD600["t4"])         # acceso por etiqueta
print(OD600.mean())        # los métodos de NumPy siguen funcionando

# DataFrame: una tabla (cada columna es una Serie) ----------------------------

# Diccionario con los datos
datos = {
    "cepa":      ["WT", "WT", "mutA", "mutB"],
    "OD600":     [1.50, 1.45, 1.30  , 1.10  ],
    "expresion": [1.0 , 1.1 , 2.4   , 0.4   ],
}

# Convertimos el dict a dataframe
df = pd.DataFrame(datos)
print(df)

# Partes de un DataFrame ------------------------------------------------------
print(df.shape)            # (filas, columnas)
print(df.columns)          # Nombres de las columnas
print(df.index)            # Etiquetas de las filas
print(df.dtypes)           # Tipo de cada columna

# Por debajo hay un array de NumPy --------------------------------------------
print(df["OD600"].to_numpy())
print(type(df["OD600"].to_numpy()))
