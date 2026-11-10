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
                raise ValueError(f"'{ID}' contiene bases invalidas: {nt}")
        
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
# ----------- Definición subclase ---------- #
##############################################

class mRNA(RNA):
    
    def __init__(self, ID, seq):
        
        RNA.__init__(self, ID, seq)
        self.CDS = self._analizar_mRNA()
        
        
    def encontrar_start(self, codon_start = "AUG"):
        
        for i in range(len(self.seq) - 2):
            if self.seq[i:i+3] == codon_start:
                return i
        return None
    
    
    def encontrar_stop(self, inicio = None, codones_stop = ["UAA", "UAG", "UGA"]):
        
        if inicio is None:
            inicio = self.encontrar_start()
        
        for i in range(inicio, len(self.seq) - 2, 3):
            codon = self.seq[i:i+3]
            if codon in codones_stop:
                return i
        return None
    
    
    def _extraer_cds(self, inicio, fin):
        return self.seq[inicio:fin]
    
    def _analizar_mRNA(self):
        
        inicio = self.encontrar_start()
        
        if inicio is None:
            raise ValueError("No se encontró codón de inicio (AUG).")
        
        fin = self.encontrar_stop(inicio)
        
        if fin is None:
            raise ValueError("No se encontró codón de stop en fase.")
            
        cds    = self._extraer_cds(inicio, fin)
        
        return cds
    
    def __str__(self):
        return ">" + str(self.ID) + "\n" + str(self.seq) + "\n" + "(CDS:" + self.CDS + ")"
        
        
    
##############################################
# ------------- Uso de la clase ------------ #
##############################################
        
# Crear rna_1 válido
rna_1 = RNA("rna_1","GCUAGCAUGUGCAAAUUGUAA")

# Crear otro RNA y compararlo con RNA_1
rna_2 = RNA("rna_2","GCUAGCAUGGCCUGCUACAAAUUGUAA")
rna_3 = RNA("rna_3","GCUAGCAUGUGCAAAUUGUAA")
rna_4 = RNA("rna_4","UACUAUUCUUACACGCUAGCAUGUGCAAAUUGUAAUACUAUUCA")


##############################################
# ------------- Uso clase mRNA ------------- #
##############################################

# Crear y ver mRNA1
mrna_1 = mRNA("mrna_1","GCUAGCAUGUGCAAAUUGUAA")
print(mrna_1)

# Intentar crear un mRNA que no tiene AUG
mrna_1 = mRNA("mrna_1","GCUAGCUUGUGCAAAUUGUAA")

# Se heredan los métodos de RNA
mrna_1 == rna_1
