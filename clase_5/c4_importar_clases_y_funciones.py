# -*- coding: utf-8 -*-

# Importamos clases dese el otro archivo (sacarle el .py)
# El archivo tiene que estár en la misma carpeta que mi modulo de ejecución
from c3_subclass_mRNA import RNA, mRNA

        
# Crear rna_1 válido
rna_1 = RNA("rna_1","GCUAGCAUGUGCAAAUUGUAA")

# Crear otro RNA y compararlo con RNA_1
rna_2 = RNA("rna_2","GCUAGCAUGGCCUGCUACAAAUUGUAA")
rna_3 = RNA("rna_3","GCUAGCAUGUGCAAAUUGUAA")
rna_4 = RNA("rna_4","UACUAUUCUUACACGCUAGCAUGUGCAAAUUGUAAUACUAUUCA")

# Crear y ver mRNA1
mrna_1 = mRNA("mrna_1","GCUAGCAUGUGCAAAUUGUAA")
print(mrna_1)

# Intentar crear un mRNA que no tiene AUG
mrna_1 = mRNA("mrna_1","GCUAGCUUGUGCAAAUUGUAA")

# Se heredan los métodos de RNA
mrna_1 == rna_1
