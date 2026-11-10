# -*- coding: utf-8 -*-

# Importamos el módulo de secuencia
from Bio.Seq import Seq

# Creamos una secuencia
mi_seq = Seq("AGTACACTGGT")

# Visualización
mi_seq
print(mi_seq)
type(mi_seq)

# Podemos usar métodos de objetos secuencia
mi_seq.complement()
mi_seq.reverse_complement()

# Podemos transcribir
mi_seq.transcribe()

# Podemos traducir a proteína
mi_seq.translate()

# Podemos contar motivos de secuencia
mi_seq.count("GT")
