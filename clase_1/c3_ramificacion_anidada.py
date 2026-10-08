# INPUT
fondo_PEIC = 6000
fraccion = 0.5
precio_replica = 500
reps = 10

presupuesto = fondo_PEIC * fraccion

# Bloque condicional
if precio_replica * reps <= presupuesto:
    print("¡El precio es razonable!")
    hacemos_experimento = True
else:
    print("¡¡¡Muy caro!!!")
    hacemos_experimento = False
    
    # Bloque anidado
    if precio_replica * (reps / 2) <= presupuesto:
        print("Pero haciendo menos réplicas...")
        print("¡El precio es razonable!")
        hacemos_experimento = True
        
# OUTPUT
print("Hacemos experimento?:", hacemos_experimento)
