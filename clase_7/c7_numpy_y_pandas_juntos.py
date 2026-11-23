# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

df = pd.read_csv("datos_levaduras.csv").dropna()

# De pandas a NumPy -----------------------------------------------------------
OD = df["OD600"].to_numpy()               # columna -> array 1D
numericas = df[["OD600", "expresion_relativa", "proteina_ug_mL"]].to_numpy()
print(OD.shape, numericas.shape)

# Funciones de NumPy directamente sobre columnas ------------------------------
print(np.mean(df["OD600"]), np.std(df["OD600"]))
print(np.log2(df["expresion_relativa"]).head())

# De NumPy a pandas -----------------------------------------------------------
rng = np.random.default_rng(seed=3)
matriz = rng.normal(loc=10, scale=2, size=(4, 3))
conteos = pd.DataFrame(matriz,
                       columns=["gen_A", "gen_B", "gen_C"],
                       index=["m1", "m2", "m3", "m4"])
print(conteos.round(2))

# Correlación entre variables -------------------------------------------------
print(np.corrcoef(df["OD600"], df["proteina_ug_mL"]))     # solo NumPy
print(df[["OD600", "expresion_relativa", "proteina_ug_mL"]].corr().round(2))
