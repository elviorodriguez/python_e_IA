# INPUT
secuencia = 'ATCGGCTAAGCTTAGCGATCGGCTAAGCTT'

# Inicializamos variables 
mas_largo_global = 0
mas_largo_actual = 0

# Iteramos sobre cada nucleótido (nt)
for nt in secuencia:
    
    # Si el nt es G, sumamos 1
    if nt == "G":
        mas_largo_actual += 1
        
        # Comparamos con el máximo encontrado hasta ahora
        if mas_largo_actual > mas_largo_global:
            mas_largo_global = mas_largo_actual
    
    # Si el nt no es G
    else:
        
        # Reiniciamos el contador
        mas_largo_actual = 0

# OUTPUT
if mas_largo_global == 0:
    print("No hay Gs!")
else:
    print("La repetición de G más larga es:", mas_largo_global)

