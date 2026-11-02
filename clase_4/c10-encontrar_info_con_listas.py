# -*- coding: utf-8 -*-

# Los elementos tienen correspondencia según índice
lista_IDs  = ['P59021' , 'P55322' , 'P63243' ]
lista_seqs = ['MTGRAAT', 'MYRGPPS', 'MLLVLIT']
lista_pIs  = [ 9.2     ,  7.4     , 4.5      ]

def recuperarInformacion(ID, lista_IDs, lista_seqs, lista_pIs):
    
    # Encontrar el indice
    indice = lista_IDs.index(ID)
    
    # Recuperar la información
    seq = lista_seqs[indice]
    pI  = lista_pIs[indice]
    
    # Entregar la información
    return (seq, pI)
        
recuperarInformacion('P55322', lista_IDs, lista_seqs, lista_pIs)

