# -*- coding: utf-8 -*-

# INPUT
secuencia = 'ATCGTATAAAAGCTTAGCGTATAAAACTAAGCTT'
motivo = 'TATAAAA'

# Inicializo un contador
numero_de_motivos = 0

# Itero sobre cada indice de la secuencia, pero freno antes de pasarme de largo
# al restarle "len(motivo) + 1" al largo de la secuencia
for i in range(len(secuencia) - len(motivo) + 1):
    
    # Extraigo el motivo de secuencia desde la posición i hasta i+len(motivo)
    if secuencia[i:i+len(motivo)] == motivo:
        
        # Si el motivo extraido es igual al motivo de busqueda, sumamos 1
        numero_de_motivos += 1
        
# OUTPUT
if numero_de_motivos == 0:
    print("No hay motivos", motivo)
else:
    print("Hay", numero_de_motivos, "motivos", motivo)