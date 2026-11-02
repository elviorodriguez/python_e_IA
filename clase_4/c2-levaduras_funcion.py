# -*- coding: utf-8 -*-

def levaduras_TiempoParaAlcanzarN(N0, Nf, t_dup = 2, epsilon = 0.1):
    
    # Variables para generar las adivinaciones y el resultado
    t_min = 0
    t_max = 200
    t = (t_min + t_max) / 2
    N = N0 * 2**(t/t_dup)
        
    # Verificamos si alcanzamos la población final
    while abs(Nf - N) > epsilon:
        
        if N < Nf:
            t_min = t
        else:
            t_max = t 
        
        # Recalculamos la población con un nuevo valor de t
        t = (t_min + t_max) / 2
        N = N0 * 2**(t/t_dup)
    
    # OUTPUT
    if Nf - N > epsilon:
        print("NO se alcanzó la población esperada.")
        print("   - Tiempo:", round(t, 2), "h")
        print("   - Población esperada (Nf):", Nf)
        print("   - Población alcanzada (N):", N)
    else:
        print("Se alcanzó la población esperada!")
        print("   - Tiempo necesario:", round(t, 2), "h")
        print("   - Población esperada (Nf):", Nf)
        print("   - Población alcanzada (N):", N)
        
    return t
    
    
# INPUT
N0 = 1000       # Células iniciales
Nf = 10000000   # Células finales

levaduras_TiempoParaAlcanzarN(N0, Nf)