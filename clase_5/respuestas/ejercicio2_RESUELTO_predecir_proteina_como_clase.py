# -*- coding: utf-8 -*-

'''
EJERCICIO 2 - Clase 5:
    
Utilizar ChatGPT, Claude, Gemini o Copilot para implementar el método 
"_predecir_proteina" de la clase mRNA y la clase "Proteina". El método 
_predecir_proteina debe devolver un objeto de clase Proteina que se genera como
atributo de los objetos de clase mRNA al crearlos.
'''

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
        self.prot = self._predecir_proteina()
        
        
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
        
    def _predecir_proteina(self):
        '''
        Predice la secuencia de proteína del mRNA y devuelve un objeto de 
        clase Proteina.

        Returns
        -------
        Protein
            Objeto de tipo Proteina con la proteína predicha como atributo.
        '''
        # Diccionario que relaciona cada codón de RNA con su aminoácido
        codigo_genetico = {
            "UUU": "F", "UUC": "F",
            "UUA": "L", "UUG": "L",
            "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
            "UAU": "Y", "UAC": "Y",
            "UGU": "C", "UGC": "C", "UGG": "W",
    
            "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
            "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
            "CAU": "H", "CAC": "H",
            "CAA": "Q", "CAG": "Q",
            "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    
            "AUU": "I", "AUC": "I", "AUA": "I",
            "AUG": "M",
            "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
            "AAU": "N", "AAC": "N",
            "AAA": "K", "AAG": "K",
            "AGU": "S", "AGC": "S",
            "AGA": "R", "AGG": "R",
    
            "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
            "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
            "GAU": "D", "GAC": "D",
            "GAA": "E", "GAG": "E",
            "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
        }
    
        # Traducimos la CDS de a tres nucleótidos (un codón por vez)
        secuencia_proteina = ""
    
        for i in range(0, len(self.CDS), 3):
            codon = self.CDS[i:i+3]
    
            # Buscamos el aminoácido correspondiente al codón
            aminoacido = codigo_genetico[codon]
    
            secuencia_proteina += aminoacido
    
        # Creamos el identificador de la proteína
        ID_prot = self.ID + "..prot"
    
        # Devolvemos un objeto de clase Proteina
        return Proteina(ID_prot, secuencia_proteina)
        
        
##############################################
# -------- Definicion clase proteína ------- #
##############################################

class Proteina:
    def __init__(self, ID, seq):
        self.ID = ID
        self.seq = seq.upper()

    def __str__(self):
        return ">" + str(self.ID) + "\n" + str(self.seq)
    
######################################################
# ------------- Testeo de la clase mRNA ------------ #
######################################################
'''
El atributo "seq" del objeto de clase Proteina asociado a cada mRNA debe
coincidir con la secuencia esperada.
'''

# Crear mRNA y testear
seq_prot_1_esperada = "MCKL"
mrna_1 = mRNA("mrna_1","GCUAGCAUGUGCAAAUUGUAA")
print(mrna_1.prot.seq == seq_prot_1_esperada)

# Crear mRNA y testear
seq_prot_2_esperada = "MAEPWKG"
mrna_2 = mRNA("mrna_2", "GGCCAUGGCUGAACCCUGGAAAGGUUGACCAUUAAA")
print(mrna_2.prot.seq == seq_prot_2_esperada)

# Crear mRNA y testear
seq_prot_3_esperada = "MLSMD"
mrna_3 = mRNA("mrna_3", "GUAACAUGCUAAGUAUGGACUAGGGGAUG")
print(mrna_3.prot.seq == seq_prot_3_esperada)

