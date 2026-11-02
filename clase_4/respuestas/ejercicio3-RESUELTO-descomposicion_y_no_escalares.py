# -*- coding: utf-8 -*-

# Clase 4: Abstracción y Descomposición con funciones
# EJERCICIO 3: Predicción de la secuencia de proteína a partir de la CDS

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

###############################################################################
# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ #
# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ #


# Modificar esta funcion para que 
def predecirProteina(cds):
    '''
    Predice la secuencia de proteína a partir de la secuencia codificante cds.

    Parameters
    ----------
    cds : str
        Secuencia codificante (ARNm: solo A, U, G y C).

    Returns
    -------
    seq_prot : str
        Secuencia de proteínas (Solo aminoácidos en "ACDEFGHIKLMNPQRSTVWY").

    '''
    
    # Diccionario con las correspondecias codon (key) -> aminoácido (value)
    codigo_genetico = {
        "UUU":"F", "UUC":"F",
        "UUA":"L", "UUG":"L", "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
        "AUU":"I", "AUC":"I", "AUA":"I",
        "AUG":"M",
        "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
        "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S", "AGU":"S", "AGC":"S",
        "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
        "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
        "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
        "UAU":"Y", "UAC":"Y",
        "CAU":"H", "CAC":"H",
        "CAA":"Q", "CAG":"Q",
        "AAU":"N", "AAC":"N",
        "AAA":"K", "AAG":"K",
        "GAU":"D", "GAC":"D",
        "GAA":"E", "GAG":"E",
        "UGU":"C", "UGC":"C",
        "UGG":"W",
        "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R",
        "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"
    }
    
    # Variable para ir agregando los aminoácido de cada codón
    seq_prot = ""
    
    # Iteramos sobre los indices (i) de cada codon
    for i in range(0, len(cds), 3):
        
        # Extraemos el codon
        codon = cds[i:i+3]
        
        # Buscamos a que aminoácido corresponde
        aminoacido = codigo_genetico[codon]
        
        # Agregamos el AA
        seq_prot += aminoacido
    
    return seq_prot
    

def predecirPesoMolecular(seq_prot):
    '''
    Predice el peso molecular a partir de la secuencia de proteínas.

    Parameters
    ----------
    seq_prot : str
        Secuencia de proteínas (Solo aminoácidos en "ACDEFGHIKLMNPQRSTVWY").

    Returns
    -------
    peso_molec_prot : float
        Peso molecular (Da).

    '''
    
    # Diccionario con los pesos moleculares (values) de cada aminoácido (keys)
    pesos_aa = {
        "A": 89.1,  "R": 174.2, "N": 132.1, "D": 133.1,
        "C": 121.2, "Q": 146.2, "E": 147.1, "G": 75.1,
        "H": 155.2, "I": 131.2, "L": 131.2, "K": 146.2,
        "M": 149.2, "F": 165.2, "P": 115.1, "S": 105.1,
        "T": 119.1, "W": 204.2, "Y": 181.2, "V": 117.1
    }
    
    # Variable para ir sumando los pesos de cada aminoácido
    peso_molec_prot = 0
    
    # Iteramos sobre la secuencia de proteínas
    for aa in seq_prot:
        # Buscamos el peso del aminoácido en el dict
        peso_molecular_aa = pesos_aa[aa]
        
        # Y lo sumamos
        peso_molec_prot += peso_molecular_aa 
    
    return peso_molec_prot

# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ #
# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ #
###############################################################################

# =============================================================================
#  FUNCIÓN ENVOLTURA: usa las funciones anteriores
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
    
    ###########################################################################
    # ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ #
    # ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ #
    
    # Generar el código para la función predecirProteina
    seq_prot = predecirProteina(cds)
    
    # Calcula el largo de la proteína
    largo_prot = len(seq_prot)
    
    # Generar el código para la función predecirPesoMolecular
    peso_molec_prot = predecirPesoMolecular(seq_prot)
    
    # ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ #
    # ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ #
    ###########################################################################
    
    print("Codón de inicio en posición:", inicio)
    print("Codón de stop   en posición:", fin)
    print("Secuencia codificante (CDS):", cds)
    print("Largo de la CDS (nt)       :", largo)
    
    # Nuevo output
    print("Secuencia de proteína      :", seq_prot)
    print("Largo de la proteína       :", largo_prot)
    print("Peso molecular (Da)        :", peso_molec_prot)
    
    return (cds, seq_prot)


# =============================================================================
#  EJECUCIÓN
# =============================================================================

# Llamado a la función de ENVOLTORIO
secuencia = "GCUAGCAUGUGCAAAUUGUAA"
analizar_mRNA(secuencia)
