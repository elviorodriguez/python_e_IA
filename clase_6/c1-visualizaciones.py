# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# Listas vacías para guardar X e Y
muestras = []
valores_lineales = []
valores_cuadraticos = []
valores_cubicos = []
valores_exponenciales = []


# Generar datos para graficar
for i in range(0, 30):
    
    # Valores para X
    muestras             .append (     i     )
    
    # Valores para Y
    valores_lineales     .append (   i       )
    valores_cuadraticos  .append (   i ** 2  )
    valores_cubicos      .append (   i ** 3  )
    valores_exponenciales.append (  1.5 ** i )

# -------------------- 1º ejemplo --------------------

# Valores de x --> muestras
# Valores de y --> valores_lineales
plt.plot(muestras, valores_lineales)


# -------------------- 2º ejemplo --------------------
# Graficar todo junto en una sola figura

plt.plot(muestras, valores_lineales)
plt.plot(muestras, valores_cuadraticos)
plt.plot(muestras, valores_cubicos)
plt.plot(muestras, valores_exponenciales)


# -------------------- 3º ejemplo --------------------
# Crear figuras distintas

plt.figure('lineal')
plt.plot(muestras, valores_lineales)

plt.figure('cuadratica')
plt.plot(muestras, valores_cuadraticos)

plt.figure('cubica')
plt.plot(muestras, valores_cubicos)

plt.figure('exponencial')
plt.plot(muestras, valores_exponenciales)


# -------------------- 4º ejemplo --------------------
plt.figure('lineal')
plt.xlabel('puntos de muestreo')
plt.ylabel('función lineal')
plt.plot(muestras, valores_lineales)

plt.figure('cuadratica')
plt.plot(muestras, valores_cuadraticos)

plt.figure('cubica')
plt.plot(muestras, valores_cubicos)

plt.figure('exponencial')
plt.plot(muestras, valores_exponenciales)

plt.figure('cuadratica')
plt.ylabel('función cuadrática')


# -------------------- 5º ejemplo --------------------
plt.figure('lineal')
plt.plot(muestras, valores_lineales)

plt.figure('cuadratica')
plt.plot(muestras, valores_cuadraticos)

plt.figure('cubica')
plt.plot(muestras, valores_cubicos)

plt.figure('exponencial')
plt.plot(muestras, valores_exponenciales)

plt.figure('lineal')
plt.title('Función lineal')

plt.figure('cuadratica')
plt.title('Función cuadrática')

plt.figure('cubica')
plt.title('Función cúbica')

plt.figure('exponencial')
plt.title('Función exponencial')


# -------------------- 6º ejemplo --------------------
plt.figure('lineal')
plt.clf()
plt.plot(muestras, valores_lineales)

plt.figure('cuadratica')
plt.clf()
plt.plot(muestras, valores_cuadraticos)

plt.figure('cubica')
plt.clf()
plt.plot(muestras, valores_cubicos)

plt.figure('exponencial')
plt.clf()
plt.plot(muestras, valores_exponenciales)

plt.figure('lineal')
plt.title('Función lineal')

plt.figure('cuadratica')
plt.title('Función cuadrática')

plt.figure('cubica')
plt.title('Función cúbica')

plt.figure('exponencial')
plt.title('Función exponencial')


# -------------------- 7º ejemplo --------------------
plt.figure('lineal')
plt.clf()
plt.ylim(0, 1000)
plt.plot(muestras, valores_lineales)

plt.figure('cuadratica')
plt.clf()
plt.ylim(0, 1000)
plt.plot(muestras, valores_cuadraticos)

plt.figure('lineal')
plt.title('Función lineal')

plt.figure('cuadratica')
plt.title('Función cuadrática')


# -------------------- 8º ejemplo --------------------
plt.figure('lineal cuadratica')
plt.clf()
plt.plot(muestras, valores_lineales)
plt.plot(muestras, valores_cuadraticos)
plt.ylabel("Crecimiento (y)")
plt.xlabel("Muestras (x)")
plt.title('Función lineal vs. cuadrática')

plt.figure('cubica exponencial')
plt.clf()
plt.plot(muestras, valores_cubicos)
plt.plot(muestras, valores_exponenciales)
plt.ylabel("Crecimiento (y)")
plt.xlabel("Muestras (x)")
plt.title('Función cúbica vs. exponencial')


# -------------------- 9º ejemplo --------------------
plt.figure('lineal cuadratica')
plt.clf()
plt.plot(muestras, valores_lineales, label='Lineal')
plt.plot(muestras, valores_cuadraticos, label='Cuadrática')
plt.legend(loc='upper right')
plt.ylabel("Crecimiento (y)")
plt.xlabel("Muestras (x)")
plt.title('Función lineal vs. cuadrática')

plt.figure('cubica exponencial')
plt.clf()
plt.plot(muestras, valores_cubicos, label='Cúbica')
plt.plot(muestras, valores_exponenciales, label='Exponencial')
plt.legend()
plt.ylabel("Crecimiento (y)")
plt.xlabel("Muestras (x)")
plt.title('Función cúbica vs. exponencial')


# -------------------- 10º ejemplo --------------------
plt.figure('lineal cuadratica')
plt.clf()
plt.plot(muestras, valores_lineales, 'b-', label='Lineal')
plt.plot(muestras, valores_cuadraticos, 'ro', label='Cuadrática')
plt.legend(loc='upper right')
plt.ylabel("Crecimiento (y)")
plt.xlabel("Muestras (x)")
plt.title('Función lineal vs. cuadrática')

plt.figure('cubica exponencial')
plt.clf()
plt.plot(muestras, valores_cubicos, 'g^', label='Cúbica')
plt.plot(muestras, valores_exponenciales, 'r--', label='Exponencial')
plt.legend()
plt.ylabel("Crecimiento (y)")
plt.xlabel("Muestras (x)")
plt.title('Función cúbica vs. exponencial')


# -------------------- 11º ejemplo --------------------
x = muestras
y = [valores_lineales, valores_cuadraticos]

plt.figure('lineal cuadratica')
plt.clf()
plt.plot(muestras, valores_lineales, 'b-', label='Lineal', linewidth=2.0)
plt.plot(muestras, valores_cuadraticos, 'r', label='Cuadrática', linewidth=3.0)
plt.legend(loc='upper right')
plt.ylabel("Crecimiento (y)")
plt.xlabel("Muestras (x)")
plt.title('Función lineal vs. función cuadrática')

plt.figure('cubica exponencial')
plt.clf()
plt.plot(muestras, valores_cubicos, 'g--', label='Cúbica', linewidth=4.0)
plt.plot(muestras, valores_exponenciales, 'r', label='Exponencial', linewidth=5.0)
plt.legend()
plt.ylabel("Crecimiento (y)")
plt.xlabel("Muestras (x)")
plt.title('Función cúbica vs. exponencial')


# -------------------- 12º ejemplo --------------------
plt.figure('cubica exponencial logaritmica')
plt.clf()
plt.plot(muestras, valores_lineales, 'b', label='Lineal', linewidth=2.0)
plt.plot(muestras, valores_cuadraticos, 'r', label='Cuadrática', linewidth=3.0)
plt.plot(muestras, valores_cubicos, 'g', label='Cúbica', linewidth=4.0)
plt.plot(muestras, valores_exponenciales, 'k', label='Exponencial', linewidth=5.0)
plt.yscale('log')
plt.legend()
plt.title('Función cúbica vs. exponencial')

plt.figure('cubica exponencial lineal')
plt.clf()
plt.plot(muestras, valores_lineales, 'b', label='Lineal', linewidth=2.0)
plt.plot(muestras, valores_cuadraticos, 'r', label='Cuadrática', linewidth=3.0)
plt.plot(muestras, valores_cubicos, 'g', label='Cúbica', linewidth=4.0)
plt.plot(muestras, valores_exponenciales, 'k', label='Exponencial', linewidth=5.0)
plt.yscale('linear')
plt.legend()
plt.title('Función cúbica vs. exponencial')

# Guardar figura
plt.savefig("cubica_vs_exponencial.png", dpi=300)


# -------------------- 13º ejemplo --------------------
# Dos filas y una columna
fig, (sub1, sub2) = plt.subplots(2, 1)

# Título, etiques y leyenda compartidas
fig.suptitle('Función lineal vs. cuadrática')
fig.supylabel("Crecimiento (y)")
fig.supxlabel("Muestras (x)")

# Subplot 1: función lineal
sub1.plot(muestras, valores_lineales, 'b-', label='Lineal', linewidth=2.0)
sub1.set_ylim(0, 900)
sub1.legend()

# Subplot 2: función cuadrática
sub2.plot(muestras, valores_cuadraticos, 'r-', label='Cuadrática', linewidth=3.0)
sub2.set_ylim(0, 900)
sub2.legend()


# Una fila y dos columnas
fig, (sub1, sub2) = plt.subplots(1, 2)

# Título, etiques y leyenda compartidas
fig.suptitle('Función cúbica vs. exponencial')
fig.supylabel("Crecimiento (y)")
fig.supxlabel("Muestras (x)")

# Subplot 1: función lineal
sub1.plot(muestras, valores_cubicos, 'b-', label='Cúbica', linewidth=2.0)
sub1.set_ylim(0, 140000)
sub1.legend()

# Subplot 2: función cuadrática
sub2.plot(muestras, valores_exponenciales, 'r-', label='Exponencial', linewidth=3.0)
sub2.set_ylim(0, 140000)
sub2.legend()