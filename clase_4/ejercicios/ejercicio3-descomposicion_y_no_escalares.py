# -*- coding: utf-8 -*-

#  Clase 4: Abstracción y Descomposición con funciones
#  EJERCICIO 3: Predicción de la secuencia de proteína a partir de la CDS

'''
Este ejercicio es una continuación del ejemplo c3 de la clase 4. En aquel
ejemplo, faltaba predecir la secuencia de la proteína a partir del CDS, el
largo de la proteína y el peso molecular de la proteína.

Para resolverlo, complete las dos nuevas funciones auxiliares:
    1) Una función debe calcular la secuencia de proteína a partir de la CDS.
       Esta debe usar una variable (un dict) que permite mapear cada codon al
       aminoácido correspondiente.
    2) La otra función calcula el peso molecular (Da) a partir de la secuencia
       de proteína. También usa una variable de tipo dict, pero que mapea el
       aminoácido al peso molecular correspondiente. La idea es devolver la
       suma de los pesos moleculares de cada aminoácido.
       
Leer la docstring de cada función auxiliar faltante para interpretar que es lo
que debería tomar como input y que dará como output. Luego, entregarle la 
docstring de cada función a la IA que utilicen siempre para que genere el
código. Reemplazar el código generado en el lugar correspondiente. Discutiremos
los resultados en clase.
'''

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


#################### MODIFICAR EL CÓDIGO DE ESTAS FUNCIONES ###################
#################### MODIFICAR EL CÓDIGO DE ESTAS FUNCIONES ###################
#################### MODIFICAR EL CÓDIGO DE ESTAS FUNCIONES ###################
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
    # Variable para ir agregando los aminoácido de cada codón
    seq_prot = ""
    
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
    
    # Variable para ir sumando los pesos de cada aminoácido
    peso_molec_prot = 0
    
    return peso_molec_prot

# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ #
# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ #
#################### MODIFICAR EL CÓDIGO DE ESTAS FUNCIONES ###################
#################### MODIFICAR EL CÓDIGO DE ESTAS FUNCIONES ###################
#################### MODIFICAR EL CÓDIGO DE ESTAS FUNCIONES ###################

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
    
    ############# ESTA SECCIÓN IMPLEMENTA LAS FUNCIONES AUXILIARES ############ 
    ############# ESTA SECCIÓN IMPLEMENTA LAS FUNCIONES AUXILIARES ############ 
    ############# ESTA SECCIÓN IMPLEMENTA LAS FUNCIONES AUXILIARES ############
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
    ############# ESTA SECCIÓN IMPLEMENTA LAS FUNCIONES AUXILIARES ############ 
    ############# ESTA SECCIÓN IMPLEMENTA LAS FUNCIONES AUXILIARES ############ 
    ############# ESTA SECCIÓN IMPLEMENTA LAS FUNCIONES AUXILIARES ############ 
    
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
