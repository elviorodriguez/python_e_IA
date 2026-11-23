# -*- coding: utf-8 -*-

'''
Ejercicio 2 - Clase 7

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
## ------------------------------ Ejercicio 2 ------------------------------ ##
###############################################################################

