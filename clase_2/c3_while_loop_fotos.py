fotos_totales = 2053
foto_actual = 1

while foto_actual <= fotos_totales:
    
    # Carga de información de la foto
    foto = "foto_" + str(foto_actual) + ".tif"
    largo_foto = len(foto)
    tipo_foto = type(foto)
    nombre_foto = foto[0:-4]
    
    # Output sobre la foto    
    print("--------- Nº de foto", foto_actual)
    print(foto)
    print(largo_foto)
    print(tipo_foto)
    print(nombre_foto)
    
    # Counter (evita quedarse en un bucle infinito)
    foto_actual = foto_actual + 1
