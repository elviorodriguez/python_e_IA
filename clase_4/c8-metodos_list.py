# -*- coding: utf-8 -*-

# Input
CDS = "AUGUGCAAAUUGAAAUGGAAA"

# Método de recolección (APPEND) ----------------------------------------------
codones = [] # <------ Lista vacía

for i in range(0, len(CDS), 3):
    codon = CDS[i:i+3]
    codones.append(codon)
    
    # Progreso
    print(codones)

# Método de recuento (COUNT) --------------------------------------------------
num_AUG = codones.count("AUG")
num_AAA = codones.count("AAA")
num_UUU = codones.count("UUU")

print("AUG:", num_AUG, "| AAA:", num_AAA, "| UUU:", num_UUU)

# Método de localización (INDEX) ----------------------------------------------
codones.index("AUG")
codones.index("AAA")
codones.index("UUU") # Da un error

# Métodos que MUTAN la lista --------------------------------------------------

# REVERSE
print(codones)
codones.reverse()   # La da vuelta
print(codones)
codones.reverse()   # La da vuelta de nuevo
print(codones)

# SORT vs SORTED
print(codones)
sorted(codones)     # Este no lo muta (devuelve una copia)
print(codones)
codones.sort()      # Este SI MUTA
print(codones)

# REMOVE
print(codones)
codones.remove("AAA")
print(codones)
codones.remove("AAA")
print(codones)
codones.remove("AAA")
print(codones)
codones.remove("AAA")   # Da un error (no quedan más codones "AAA")
print(codones)

# COPIAS y ALIAS --------------------------------------------------------------

# Esto crea un ALIAS
triadas = codones
print(triadas)
print(codones)

# Apuntan al mismo objeto
triadas.append("UGA")
print(triadas)
print(codones)

# Esto crea una copia
triadas = codones.copy()
triadas.append("GGG")
print(triadas)
print(codones)




