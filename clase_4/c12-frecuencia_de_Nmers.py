# -*- coding: utf-8 -*-

def frecuenciaNmers(seq, N = 2):
    '''
    Calcula la frecuencia de motivos tamaño N (N-mers) en la secuencia seq.

    Parameters
    ----------
    seq : str
        Secuencia de nt o proteínas.
    N : int
        Tamaño de los motivos que se desea contabilizar.

    Returns
    -------
    Nmers : dict
        Diccionario con frecuencias de motivos. Las keys son los motivos y los 
        valores son la frecuencia de cada motivo.

    '''
    
    # Inicializamos el dict
    Nmers = {}
    
    # Contamos por cada ventana de tamaño N
    for i in range(0, len(seq) - N):
        
        # Extraemos el N-mer de la posición i
        motivo = seq[i:i+N]
        
        # Si el motivo todavía no está en el dict
        if motivo not in Nmers:
            
            # Lo agregamos y contamos 1
            Nmers[motivo] = 1
        
        # Si el motivo ya estaba en el dict
        else:
            
            # Sumamos 1
            Nmers[motivo] += 1
            
    return Nmers



# INPUT
seq = "CGCGTACGATAGCGCGGCGTCGACGACGACGCGT"

# Calculo de frecuencias
frecuencias = frecuenciaNmers(seq, N = 2)


