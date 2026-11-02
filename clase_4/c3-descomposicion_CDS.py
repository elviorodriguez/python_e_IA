# -*- coding: utf-8 -*-

#  Clase 4: Abstracción y Descomposición con funciones
#  EJEMPLO: Extracción de la secuencia codificante

# =============================================================================
# FUNCIONES AUXILIARES: descomposición de la tarea de buscar el CDS
# =============================================================================

def encontrar_start(mrna):
    """
    Busca la posición del primer codón de inicio (AUG) en la secuencia.

    Input:  mrna (str) - secuencia de ARNm en mayúsculas (ej: "GCAAUGCGA")
    Output: (int) - índice donde comienza el AUG, o None si no se encuentra
    """
    for i in range(len(mrna) - 2):
        if mrna[i:i+3] == "AUG":
            return i
    return None


def encontrar_stop(mrna, inicio):
    """
    Busca el primer codón de stop (UAA, UAG, UGA) en fase con el AUG.

    Input:  mrna   (str) - secuencia de ARNm en mayúsculas
            inicio (int) - posición donde comienza la lectura (el AUG)
    Output: (int) - índice donde comienza el codón de stop, o None si no hay
    """
    
    for i in range(inicio, len(mrna) - 2, 3):
        codon = mrna[i:i+3]
        if codon == "UAA" or codon == "UAG" or codon == "UGA":
            return i
    return None


def extraer_cds(mrna, inicio, fin):
    """
    Extrae la secuencia codificante entre el AUG y el codón de stop.
    Incluye el AUG pero NO incluye el codón de stop.

    Input:  mrna   (str) - secuencia de ARNm en mayúsculas
            inicio (int) - índice del AUG
            fin    (int) - índice del codón de stop
    Output: (str) - secuencia codificante
    """
    return mrna[inicio:fin]


def calcular_largo(cds):
    """
    Calcula el largo de la secuencia codificante en nucleótidos.

    Input:  cds (str) - secuencia codificante
    Output: (int) - número de nucleótidos
    """
    return len(cds)


# =============================================================================
#  FUNCIÓN ENVOLTURA: usa las cuatro funciones anteriores
# =============================================================================

def analizar_mRNA(mrna):
    """
    Analiza un ARNm y extrae información sobre su secuencia codificante.

    A partir de una secuencia de ARNm, identifica el codón de inicio,
    el codón de stop y extrae la región codificante (CDS), reportando
    su largo en nucleótidos.

    Input:  mrna (str) - secuencia de ARNm en mayúsculas
    Output: None - imprime los resultados en pantalla
    """
    inicio = encontrar_start(mrna)
    
    if inicio is None:
        print("No se encontró codón de inicio (AUG).")
        return None
    
    fin = encontrar_stop(mrna, inicio)
    
    if fin is None:
        print("No se encontró codón de stop en fase.")
        return None
    
    cds   = extraer_cds(mrna, inicio, fin)
    largo = calcular_largo(cds)
    
    print("Codón de inicio en posición:", inicio)
    print("Codón de stop   en posición:", fin)
    print("Secuencia codificante (CDS):", cds)
    print("Largo de la CDS (nt)       :", largo)
    
    # Estos los resolveremos después usando NO-escalares
    print("Secuencia de proteína      : ¿¿¿???")
    print("Largo de la proteína       : ¿¿¿???")
    print("Peso molecular (Da)        : ¿¿¿???")


# =============================================================================
#  EJECUCIÓN
# =============================================================================

# Llamado a la función de ENVOLTORIO
secuencia = "GCUAGCAUGUGCAAAUUGUAA"
analizar_mRNA(secuencia)


# Las funciones AUXILIARES se pueden probar solas, sin necesidad del resto:
print(encontrar_start("GCAAUGCGA"))   # → 3
print(encontrar_stop("AUGCGAUAA", 0)) # → 6
