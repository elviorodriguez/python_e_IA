# -*- coding: utf-8 -*-

##############################################
# --------- Definición de la clase --------- #
##############################################
class RNA(object):
    
    def __init__(self, ID, seq):
        
        # Verificamos que la secuencia sea válida
        nt_validos = ["U", "A", "C", "G", "u", "a", "c", "g"]
        for nt in seq:
            if nt not in nt_validos:
                raise ValueError(
                    f"La secuencia de RNA para el ID '{ID}' contiene bases invalidas: {nt}"
                )
        
        # Asociar atributos
        self.ID  = ID
        self.seq = seq.upper()

    def __str__(self):
        return ">" + str(self.ID) + "\n" + str(self.seq)
    
    def contar_nt(self, nt_a_contar = "G"):
        
        total = 0
        for nt in self.seq:
            if nt == nt_a_contar:
                total += 1
        return total
    
    def porcentaje_nt(self, nt_a_contar = "G"):
        
        total = self.contar_nt(nt_a_contar)
        largo_seq = len(self.seq)
        porcentaje = total / largo_seq * 100
        
        return porcentaje
    
    def __eq__(self, other):
        return self.seq == other.seq
    
    def esta_en(self, other):
        return self.seq in other.seq
    
    
##############################################
# ------------- Uso de la clase ------------ #
##############################################
    
        
# Crear rna_1 válido
rna_1 = RNA("rna_1","GCUAGCAUGUGCAAAUUGUAA")

# Crear rna_1 inválido
rna_invalido = RNA("rna_invalido","GCUAGCAUxxxxxGUGCAAAUUGUAA")

# Acceder a los atributos
rna_1.ID
rna_1.seq

# Representación rna_1
print(rna_1)

# Contar nt o porcentaje de nt
rna_1.contar_nt()
rna_1.porcentaje_nt()

# Contar C o porcentaje de C
rna_1.contar_nt("C")
rna_1.porcentaje_nt("C")

# Crear otro RNA y compararlo con RNA_1
rna_2 = RNA("rna_2","GCUAGCAUGGCCUGCUACAAAUUGUAA")
rna_3 = RNA("rna_3","GCUAGCAUGUGCAAAUUGUAA")
rna_4 = RNA("rna_4","UACUAUUCUUACACGCUAGCAUGUGCAAAUUGUAAUACUAUUCA")

rna_1 == rna_2
rna_1 == rna_3

rna_1.esta_en(rna_3)
rna_1.esta_en(rna_4)
