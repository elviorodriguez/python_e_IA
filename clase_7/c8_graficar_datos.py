# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.read_csv("datos_levaduras.csv").dropna()

# Vemos el dataframe
print(df)

###############################################################################
# -------------------------- Correlación OD/Prot ---------------------------- #
###############################################################################

# -------------------------- Gráfico OD vs Prot -------------------------------

# Esto devuelve una figura
fig_OD_vs_P = df.plot(
    kind="scatter",
    x="OD600",
    y="proteina_ug_mL"
)

fig_OD_vs_P.set_xlabel("OD600")
fig_OD_vs_P.set_ylabel("Proteína (μg/mL)")
fig_OD_vs_P.set_title("Correlación entre OD600 y proteína")

# ------------------------ Correlación OD vs prot -----------------------------

# Ajuste lineal de grado 1 con polyfit
pendiente, ordenada = np.polyfit(x = df["OD600"],
                                 y = df["proteina_ug_mL"],
                                 deg = 1)

# Generamos valores de X e Y para la linea
ajuste_x = np.array([df["OD600"].min(),  df["OD600"].max()])
ajuste_y = ajuste_x * pendiente + ordenada

# Sumamos la nueva capa
fig_OD_vs_P.plot(ajuste_x, ajuste_y, 'k--', linewidth = 1)


###############################################################################
# --------------------------- Graficos de barra ----------------------------- #
###############################################################################

# ------------------------------- Estadísticas --------------------------------

# Agrupamos y calculamos estadísticas por cepa y condición
df_estadisticas = df.groupby(['cepa','condicion']).agg(
    
    # Calculamos la media y el desvío estandar para cada parámetro
    OD_media = ("OD600", "mean"),
    OD_std   = ("OD600", "std"),
    
    ER_media = ("expresion_relativa", "mean"),
    ER_std   = ("expresion_relativa", "std"),
    
    Prot_media = ("proteina_ug_mL", "mean"),
    Prot_std   = ("proteina_ug_mL", "std")
)


# ---------------------------------- OD600 ------------------------------------

# Pasamos 'condicion' a columnas para tener una barra por condición
medias1 = df_estadisticas["OD_media"].unstack("condicion")
desvios1 = df_estadisticas["OD_std"].unstack("condicion")

# Gráfico de barras con barras de error (media ± std)
fig1 = medias1.plot(
    kind="bar",     # Tipo de gráfico
    yerr=desvios1,   # Error en el eje y
    capsize=4,          # Agrega extremo de las barras de error
    figsize=(7, 5),     # Tamaño de la figura
    edgecolor="black"   # Borde negro de las barras
)

fig1.set_xlabel("Cepa")
fig1.set_ylabel("OD600")
fig1.set_title("Crecimiento por cepa y condición (media ± std)")
fig1.legend(title="Condición")


# ------------------------- Expresión relativa (ER) ---------------------------

# Pasamos 'condicion' a columnas para tener una barra por condición
medias2 = df_estadisticas["ER_media"].unstack("condicion")
desvios2 = df_estadisticas["ER_std"].unstack("condicion")

# Gráfico de barras con barras de error (media ± std)
fig2 = medias2.plot(
    kind="bar",     # Tipo de gráfico
    yerr=desvios2,   # Error en el eje y
    capsize=4,          # Barrita
    figsize=(7, 5),     # Tamaño de la figura
    edgecolor="black"   # Borde negro de las barras
)

fig2.set_xlabel("Cepa")
fig2.set_ylabel("Expresión relativa (ER)")
fig2.set_title("ER por cepa y condición (media ± std)")
fig2.legend(title="Condición")

# --------------------------------- Proteínas ---------------------------------

# Pasamos 'condicion' a columnas para tener una barra por condición
medias3 = df_estadisticas["Prot_media"].unstack("condicion")
desvios3 = df_estadisticas["Prot_std"].unstack("condicion")

# Gráfico de barras con barras de error (media ± std)
fig3 = medias3.plot(
    kind="bar",     # Tipo de gráfico
    yerr=desvios3,   # Error en el eje y
    capsize=4,          # Barrita
    figsize=(7, 5),     # Tamaño de la figura
    edgecolor="black"   # Borde negro de las barras
)

fig3.set_xlabel("Cepa")
fig3.set_ylabel("Proteína (μg/mL)")
fig3.set_title("Proteína por cepa y condición (media ± std)")
fig3.legend(title="Condición")
