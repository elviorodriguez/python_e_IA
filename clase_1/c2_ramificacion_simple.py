# INPUT
fondo_PEIC = 6000
fraccion = 0.5
precio_experimento = 5000

# Bloque condicional
if precio_experimento <= fondo_PEIC * fraccion:
    print("¡El precio es razonable!")
    hacemos_experimento = True
else:
    print("¡¡¡Muy caro!!!")
    hacemos_experimento = False

# OUTPUT
print("Hacemos experimento?:", hacemos_experimento)
