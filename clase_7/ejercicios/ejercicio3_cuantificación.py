# -*- coding: utf-8 -*-

'''
Ejercicio 3 - Clase 7

Seguir las instrucciones discutidas en clase. Utilizar IA para generar el 
código.
'''

import pandas as pd
import string

###############################################################################
## ------------------- Parte del ejercicio 1 - NO TOCAR -------------------- ##
###############################################################################

# Archivos
archivo_etiquetas = 'ej1_labels.tsv'
archivo_abs550 = 'ej1_abs550.tsv'

# 1) Cargar ambos archivos (sin encabezado; las absorbancias usan coma decimal)
etiquetas = pd.read_csv(archivo_etiquetas, sep='\t', header=None, dtype=str)
abs550 = pd.read_csv(archivo_abs550, sep='\t', header=None)

# Nombres de pocillos: filas A-H, columnas 1-12 (placa de 96)
etiquetas.index = list(string.ascii_uppercase[:etiquetas.shape[0]])
etiquetas.columns = range(1, etiquetas.shape[1] + 1)
abs550.index = etiquetas.index
abs550.columns = etiquetas.columns

# 2) Pasar a formato largo y combinar en un único dataframe
df_labels = etiquetas.stack().rename('label')
df_abs = abs550.stack().rename('abs550')

df = pd.concat([df_labels, df_abs], axis=1).reset_index()
df['pocillo'] = df['level_0'] + df['level_1'].astype(str)
df = df[['pocillo', 'label', 'abs550']]

# 3) Descartar pocillos sin label
df = df.dropna(subset=['label']).reset_index(drop=True)

print(df)

###############################################################################
## ------------------- Parte del ejercicio 2 - NO TOCAR -------------------- ##
###############################################################################

import numpy as np
import matplotlib.pyplot as plt

# Promedio de absorbancia de los blancos
blank_mean = df.loc[df['label'] == 'blank', 'abs550'].mean()

# Quedarse solo con las filas de label numérica (concentración)
df['conc'] = pd.to_numeric(df['label'], errors='coerce')
calib = df.dropna(subset=['conc']).copy()

# Restar el blank
calib['abs550_corr'] = calib['abs550'] - blank_mean

# Regresión lineal: abs550_corr = pendiente * conc + ordenada
pendiente, ordenada = np.polyfit(calib['conc'], calib['abs550_corr'], deg=1)

# R2 = 1 - SS_residual / SS_total
pred = pendiente * calib['conc'] + ordenada
ss_res = np.sum((calib['abs550_corr'] - pred) ** 2)
ss_tot = np.sum((calib['abs550_corr'] - calib['abs550_corr'].mean()) ** 2)
r2 = 1 - ss_res / ss_tot

print(f'blank = {blank_mean:.4f}')
print(f'pendiente = {pendiente:.6g} | ordenada = {ordenada:.6g} | R2 = {r2:.4f}')

# Gráfico
x = np.linspace(0, calib['conc'].max(), 100)
fig, ax = plt.subplots(figsize=(6, 4.5))
ax.scatter(calib['conc'], calib['abs550_corr'], label='Réplicas')
ax.plot(x, pendiente * x + ordenada, 'r-',
        label=f'y = {pendiente:.3g}x + {ordenada:.3g}\n$R^2$ = {r2:.4f}')
ax.set_xlabel('Concentración')
ax.set_ylabel('Abs550 - blank')
ax.set_title('Curva de calibración')
ax.legend()
fig.tight_layout()
plt.show()

###############################################################################
## ------------------------------ Ejercicio 3 ------------------------------ ##
###############################################################################