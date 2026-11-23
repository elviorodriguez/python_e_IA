# -*- coding: utf-8 -*-

"""
Se le dió a Claude Sonnet 5.5 (Esfuerzo: Bajo) la siguiente prompt y se le 
compartió el archivo 'ejercicio4_cuantificación_con_cli.py':
    
Convierte el código adjunto a un script ejecutable desde la linea de comando
utilizando if __name__ == "__main__" y argparse para tomar como input los
archivos de labels y abs550.
"""

############### Código de Claude:

'''
Ejercicio 4 - Clase 7

Calcula la curva de calibración a partir de una placa de 96 pocillos y estima
la concentración de las muestras.

Uso:
    python curva_calibracion.py ej1_labels.tsv ej1_abs550.tsv
    python curva_calibracion.py ej1_labels.tsv ej1_abs550.tsv -o salida.txt --no-plot
'''

import argparse
import string

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def cargar_datos(archivo_etiquetas, archivo_abs550):
    """Carga ambos archivos y los combina en un dataframe en formato largo."""
    # Sin encabezado
    etiquetas = pd.read_csv(archivo_etiquetas, sep='\t', header=None, dtype=str)
    abs550 = pd.read_csv(archivo_abs550, sep='\t', header=None)

    # Nombres de pocillos: filas A-H, columnas 1-12 (placa de 96)
    etiquetas.index = list(string.ascii_uppercase[:etiquetas.shape[0]])
    etiquetas.columns = range(1, etiquetas.shape[1] + 1)
    abs550.index = etiquetas.index
    abs550.columns = etiquetas.columns

    # Formato largo
    df_labels = etiquetas.stack().rename('label')
    df_abs = abs550.stack().rename('abs550')

    df = pd.concat([df_labels, df_abs], axis=1).reset_index()
    df['pocillo'] = df['level_0'] + df['level_1'].astype(str)
    df = df[['pocillo', 'label', 'abs550']]

    # Descartar pocillos sin label
    return df.dropna(subset=['label']).reset_index(drop=True)


def calcular_curva(df):
    """Ajusta la curva de calibración. Devuelve blank, pendiente, ordenada, R2 y calib."""
    blank_mean = df.loc[df['label'] == 'blank', 'abs550'].mean()

    # Solo filas con label numérica (concentración)
    df['conc'] = pd.to_numeric(df['label'], errors='coerce')
    calib = df.dropna(subset=['conc']).copy()
    calib['abs550_corr'] = calib['abs550'] - blank_mean

    # abs550_corr = pendiente * conc + ordenada
    pendiente, ordenada = np.polyfit(calib['conc'], calib['abs550_corr'], deg=1)

    pred = pendiente * calib['conc'] + ordenada
    ss_res = np.sum((calib['abs550_corr'] - pred) ** 2)
    ss_tot = np.sum((calib['abs550_corr'] - calib['abs550_corr'].mean()) ** 2)
    r2 = 1 - ss_res / ss_tot

    return blank_mean, pendiente, ordenada, r2, calib


def graficar_calibracion(calib, pendiente, ordenada, r2):
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


def calcular_muestras(df, blank_mean, pendiente, ordenada):
    """Interpola la concentración de las muestras (label no numérica y != 'blank')."""
    muestras = df[df['conc'].isna() & (df['label'] != 'blank')].copy()
    muestras['abs550_corr'] = muestras['abs550'] - blank_mean
    muestras['conc_calc'] = (muestras['abs550_corr'] - ordenada) / pendiente
    resumen = muestras.groupby('label')['conc_calc'].mean()
    return muestras, resumen


def graficar_muestras(calib, muestras, resumen, pendiente, ordenada, r2):
    x = np.linspace(0, calib['conc'].max(), 100)
    fig, ax = plt.subplots(figsize=(8, 5.5))
    ax.scatter(calib['conc'], calib['abs550_corr'], color='black', label='Calibración')
    ax.plot(x, pendiente * x + ordenada, 'k-',
            label=f'y = {pendiente:.3g}x + {ordenada:.3g}\n$R^2$ = {r2:.4f}')

    colores = plt.cm.tab20(np.linspace(0, 1, resumen.size))
    for color, etiqueta in zip(colores, resumen.index):
        sub = muestras[muestras['label'] == etiqueta]
        ax.scatter(sub['conc_calc'], sub['abs550_corr'], color=color,
                   marker='s', label=etiqueta)

    ax.set_xlabel('Concentración')
    ax.set_ylabel('Abs550 - blank')
    ax.set_title('Curva de calibración y muestras')
    ax.legend(fontsize=8, ncol=2)
    fig.tight_layout()


def guardar_resultados(archivo_salida, blank_mean, pendiente, ordenada, r2, resumen):
    lineas = [f'Blank (promedio abs550): {blank_mean:.4f}',
              f'Curva: abs550_corr = {pendiente:.6g} * conc + {ordenada:.6g} (R2 = {r2:.4f})',
              '',
              'Concentración promedio por etiqueta:']
    lineas += [f'{etiqueta}\t{conc:.2f}' for etiqueta, conc in resumen.items()]
    texto = '\n'.join(lineas)

    print(texto)
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write(texto + '\n')


def parsear_argumentos():
    parser = argparse.ArgumentParser(
        description='Curva de calibración y estimación de concentraciones '
                    'a partir de una placa de 96 pocillos.')
    parser.add_argument('archivo_etiquetas',
                        help='Archivo .tsv con las etiquetas de los pocillos (ej: ej1_labels.tsv)')
    parser.add_argument('archivo_abs550',
                        help='Archivo .tsv con las absorbancias a 550 nm (ej: ej1_abs550.tsv)')
    parser.add_argument('-o', '--salida', default='resultados_concentracion.txt',
                        help='Archivo de texto de salida (default: %(default)s)')
    parser.add_argument('--no-plot', action='store_true',
                        help='No mostrar los gráficos')
    return parser.parse_args()


def main():
    args = parsear_argumentos()

    df = cargar_datos(args.archivo_etiquetas, args.archivo_abs550)
    print(df)

    blank_mean, pendiente, ordenada, r2, calib = calcular_curva(df)
    print(f'blank = {blank_mean:.4f}')
    print(f'pendiente = {pendiente:.6g} | ordenada = {ordenada:.6g} | R2 = {r2:.4f}')

    muestras, resumen = calcular_muestras(df, blank_mean, pendiente, ordenada)
    guardar_resultados(args.salida, blank_mean, pendiente, ordenada, r2, resumen)

    if not args.no_plot:
        graficar_calibracion(calib, pendiente, ordenada, r2)
        graficar_muestras(calib, muestras, resumen, pendiente, ordenada, r2)
        plt.show()


if __name__ == '__main__':
    main()