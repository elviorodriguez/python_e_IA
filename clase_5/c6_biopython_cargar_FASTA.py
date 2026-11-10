# -*- coding: utf-8 -*-

# Cargar paquete INPUT y OUTPUT de secuencias (SeqIO)
from Bio import SeqIO

##################### SeqIO.parse genera un iterador ##########################

# Cargamos el archivo como un iterador
iterador_FASTA = SeqIO.parse("ls_orchid.fasta", "fasta")

# Debemos ir generando secuencia por secuencia (se va vaciando)
for seq_record in iterador_FASTA:
    print(seq_record.id)
    print(seq_record.seq)
    print(len(seq_record.seq))

###################### Generar una lista de SeqRecords ########################
   
# Se puede convertir a lista, pero ahora está vacío
lista_seq_record = list(iterador_FASTA)
    
# Cargamos el archivo de nuevo
iterador_FASTA = SeqIO.parse("ls_orchid.fasta", "fasta")    
lista_seq_record = list(iterador_FASTA)

# Podemos acceder a cada SeqRecord usando indexado
seq_record_0 = lista_seq_record[0]
type(seq_record_0)

# Acceder a los atributos
type(seq_record_0.seq)
type(seq_record_0.id)
type(seq_record_0.features)     # <------ Anotaciones (solo en formato gbk)

# Usar los métodos de Seq, no los de SeqRecord
seq_record_0.seq.reverse_complement()
seq_record_0.seq.transcribe()
seq_record_0.seq.translate()
