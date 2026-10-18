
# INPUT
secuencia = ''

num_A = 0
num_T = 0
num_C = 0
num_G = 0

# Iteramos sobre la secuencia, nucleotido a nucleotido
for nt in secuencia:
    
    # Identificamos de que nt se trata y sumamos 1 al que corresponda
    if nt == "A":
        num_A += 1
    elif nt == "T":
        num_T += 1
    elif nt == "C":
        num_C += 1
    elif nt == "G":
        num_G += 1
    else:
        print("Nucleotido desconocido:", nt)
        
# Hacemos el calculo de %
largo_secuencia = len(secuencia)
if largo_secuencia != 0:
    porcentaje_A = num_A / largo_secuencia * 100
    porcentaje_T = num_T / largo_secuencia * 100
    porcentaje_C = num_C / largo_secuencia * 100
    porcentaje_G = num_G / largo_secuencia * 100
else:
    porcentaje_A = 0
    porcentaje_T = 0
    porcentaje_C = 0
    porcentaje_G = 0

# OUTPUT
print("% A =", porcentaje_A)
print("% T =", porcentaje_T)
print("% C =", porcentaje_C)
print("% G =", porcentaje_G)

# Corroboramos
print("% total =",porcentaje_A+porcentaje_T+porcentaje_C+porcentaje_G)


###############################################################################
# ------------------- Dataset de prueba para copiar y pegar ----------------- #
###############################################################################
# Si anda con todos estos ejemplos, entonces, el programa funciona

# Esperado: A = 100, T: 0, C: 0, G: 0
secuencia = 'AAAAA'

# Esperado: A = 100, T: 0, C: 0, G: 0
secuencia = 'A'

# Esperado: A = 0, T: 100, C: 0, G: 0
secuencia = 'TTTTT'

# Esperado: A = 0, T: 100, C: 0, G: 0
secuencia = 'T'

# Esperado: A = 0, T: 0, C: 100, G: 0
secuencia = 'CCCCC'

# Esperado: A = 0, T: 0, C: 100, G: 0
secuencia = 'C'

# Esperado: A = 0, T: 0, C: 0, G: 100
secuencia = 'GGGGG'

# Esperado: A = 0, T: 0, C: 0, G: 100
secuencia = 'G'

# Esperado: A = 0, T: 0, C: 0, G: 0
secuencia = ''

# Esperado: A = 25, T: 25, C: 25, G: 25
secuencia = 'ATCG'

# Esperado: A = 50, T: 0, C: 0, G: 50
secuencia = 'GAGAGA'