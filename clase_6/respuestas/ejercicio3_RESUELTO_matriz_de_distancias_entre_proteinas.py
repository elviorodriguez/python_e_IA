# -*- coding: utf-8 -*-

# PROMPT UTILIZADA Claude Opus 5.5 (Esfuerzo Medio):
'''
Hola! Me ayudarías a generar el código de las siguientes funciones?


# Primer funcion
def cargar_fasta(fasta):
    """
    Carga un archivo fasta y lo convierte en una lista de objetos de tipo 
    SeqRecord que contienen las secuencias de proteínas y los IDs del header.

    Parameters
    ----------
    fasta : str
        Camino al archivo FASTA con secuencias de proteínas.

    Returns
    -------
    lista_secuencias : list[SeqRecord]
        Lista de objetos SeqRecord de Biopython con secuencias de proteínas.
    """


# Segunda función
def calcular_matriz_de_similitud(lista_secuencias):
    """
    Convierte la lista de secuencias a una matriz de similitud utilizando
    los scores producto de alineamientos pareados. Los valores de similitud
    representan la similtud normalizada de los scores.
    
    ALTOS VALORES = ALTA SIMILITUD DE SECUENCIA

    Parameters
    ----------
    lista_secuencias : list[SeqRecord]
        Lista de objetos SeqRecord de Biopython con secuencias de proteínas.

    Returns
    -------
    matriz_de_similitud : np.array 2D
        Matriz len(lista_secuencias) x len(lista_secuencias) de similitud
        entre las proteínas, manteniendo el orden de lista_secuencias.
    """
    
    

# Tercera función
def graficar_matriz_de_similitud(lista_secuencias, matriz_de_similitud):
    """
    Grafica la matriz de similitud como mapa de calor con los nombres de las
    proteínas (IDs) en los ejes X e Y.

    Parameters
    ----------
    lista_secuencias : list[SeqRecord]
        Lista de objetos SeqRecord de Biopython con secuencias de proteínas.
    matriz_de_similitud : np.array 2D
        Matriz len(lista_secuencias) x len(lista_secuencias) de similitud
        entre las proteínas, manteniendo el orden de lista_secuencias.

    Returns
    -------
    None
    """
    

###############################################################################
# --------------------- Función principal (envoltorio) ---------------------- #
###############################################################################

# Función de envoltorio
def graficar_matriz_de_similitud_desde_fasta(fasta):
    
    lista_secuencias = cargar_fasta(fasta)
    matriz_de_distancias = calcular_matriz_de_similitud(lista_secuencias)
    graficar_matriz_de_similitud(lista_secuencias, matriz_de_distancias)
    

###############################################################################
# -------------------------------- EJECUCIÓN -------------------------------- #
###############################################################################

# INPUT
fasta = 'ejercicio3_base_de_datos.fasta'

# Ejecución
graficar_matriz_de_similitud_desde_fasta(fasta)


Te comparto como quiero que se hagan algunas cosas (archivos adjuntos).
'''

# SE LE COMPARTIÓ COMO ARCHIVOS ADJUNTOS:
'''
clase_5/c7_biopython_alineamientos.py
clase_5/c5_biopython_introduccion.py
clase_5/c6_biopython_cargar_FASTA.py
clase_6/c8-visualizar_numpy_arrays_con_lables.py
'''

import numpy as np
import matplotlib.pyplot as plt
from Bio import SeqIO
from Bio.Align import PairwiseAligner
from Bio.Align import substitution_matrices


###############################################################################
# -------------------------- Funciones auxiliares --------------------------- #
###############################################################################

# Primer funcion
def cargar_fasta(fasta):
    """
    Carga un archivo fasta y lo convierte en una lista de objetos de tipo 
    SeqRecord que contienen las secuencias de proteínas y los IDs del header.

    Parameters
    ----------
    fasta : str
        Camino al archivo FASTA con secuencias de proteínas.

    Returns
    -------
    lista_secuencias : list[SeqRecord]
        Lista de objetos SeqRecord de Biopython con secuencias de proteínas.
    """
    
    # Cargamos el archivo como un iterador
    iterador_FASTA = SeqIO.parse(fasta, "fasta")
    
    # Convertimos el iterador a lista de SeqRecords
    lista_secuencias = list(iterador_FASTA)
    
    return lista_secuencias

# Segunda función
def calcular_matriz_de_similitud(lista_secuencias):
    """
    Convierte la lista de secuencias a una matriz de similitud utilizando
    los scores producto de alineamientos pareados. Los valores de similitud
    representan la similtud normalizada de los scores.
    
    ALTOS VALORES = ALTA SIMILITUD DE SECUENCIA

    Parameters
    ----------
    lista_secuencias : list[SeqRecord]
        Lista de objetos SeqRecord de Biopython con secuencias de proteínas.

    Returns
    -------
    matriz_de_similitud : np.array 2D
        Matriz len(lista_secuencias) x len(lista_secuencias) de similitud
        entre las proteínas, manteniendo el orden de lista_secuencias.
    """
    
    
    # ------------------- Configurar el alineador ------------------- #
    
    # Cargar el alineador en modo local
    aligner = PairwiseAligner()
    aligner.mode = "global"
    
    # Matriz de sustitución para proteínas y penalidades de gaps
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    
    # ------------- Scores de cada secuencia contra sí misma ------------- #
    
    # Cantidad de secuencias
    n = len(lista_secuencias)
    
    # Score máximo posible de cada secuencia (alinearla consigo misma)
    auto_scores = []
    for seq_record in lista_secuencias:
        auto_scores.append(aligner.score(seq_record.seq, seq_record.seq))
    
    # ------------------- Llenar la matriz de similitud ------------------- #
    
    # Matriz vacía de n x n
    matriz_de_similitud = np.zeros((n, n))
    
    # Recorremos solo la mitad superior (la matriz es simétrica)
    for i in range(n):
        for j in range(i, n):
            
            # Score del alineamiento entre la secuencia i y la j
            score = aligner.score(lista_secuencias[i].seq, 
                                  lista_secuencias[j].seq)
            
            # Normalizamos con los auto-scores (valores entre 0 y 1)
            similitud = score / np.sqrt(auto_scores[i] * auto_scores[j])
            
            # Guardamos el valor en ambas posiciones
            matriz_de_similitud[i, j] = similitud
            matriz_de_similitud[j, i] = similitud
    
    return matriz_de_similitud
    

# Tercera función
def graficar_matriz_de_similitud(lista_secuencias, matriz_de_similitud):
    """
    Grafica la matriz de similitud como mapa de calor con los nombres de las
    proteínas (IDs) en los ejes X e Y.

    Parameters
    ----------
    lista_secuencias : list[SeqRecord]
        Lista de objetos SeqRecord de Biopython con secuencias de proteínas.
    matriz_de_similitud : np.array 2D
        Matriz len(lista_secuencias) x len(lista_secuencias) de similitud
        entre las proteínas, manteniendo el orden de lista_secuencias.

    Returns
    -------
    None
    """
        
    # Nombres de las proteínas (IDs del header)
    nombres = [seq_record.id for seq_record in lista_secuencias]
    
    # Mapa de calor
    plt.imshow(matriz_de_similitud, cmap='viridis', vmin=0, vmax=1)
    plt.colorbar(label='Similitud')
    plt.title('Matriz de similitud de proteínas')
    
    # Etiquetas de ejes
    plt.xticks(range(len(nombres)), nombres, rotation=90)
    plt.yticks(range(len(nombres)), nombres)
    
    # Ajustar márgenes para que entren los nombres
    plt.tight_layout()
    
    plt.show()
    

###############################################################################
# --------------------- Función principal (envoltorio) ---------------------- #
###############################################################################

# Función de envoltorio
def graficar_matriz_de_similitud_desde_fasta(fasta):
    
    lista_secuencias = cargar_fasta(fasta)
    matriz_de_distancias = calcular_matriz_de_similitud(lista_secuencias)
    graficar_matriz_de_similitud(lista_secuencias, matriz_de_distancias)
    

###############################################################################
# -------------------------------- EJECUCIÓN -------------------------------- #
###############################################################################

# INPUT
fasta = 'ejercicio3_base_de_datos.fasta'

# Ejecución
graficar_matriz_de_similitud_desde_fasta(fasta)





