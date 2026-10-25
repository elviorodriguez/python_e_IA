def levaduras_TiempoParaAlcanzarN(N0, Nf, t_dup=2):
    '''
    Conociendo el tiempo de duplicación de una cepa de levaduras (t_dup) y el
    número de células iniciales (N0), calcula el tiempo de incubación necesario
    (t) para alcanzar un número de levaduras Nf. Asume crecimiento exponencial.

    Parameters
    ----------
    N0 : float|int
        Población inicial de levaduras. Número absoluto (no es concentración).
    Nf : float|int
        Población final de levaduras luego del tiempo t. Número absoluto (no es
        concentración).
    t_dup : float|int, optional
        Tiempo de duplicación de la cepa de levaduras (horas). El valor por 
        defecto es 2.

    Returns
    -------
    t : float
        Tiempo necesario (horas) para alcanzar la población Nf a partir de N0
        con un tiempo de duplicación t_dup (horas).
    '''

    # Validaciones básicas
    if N0 <= 0:
        raise ValueError("N0 debe ser mayor que cero.")
    if Nf <= 0:
        raise ValueError("Nf debe ser mayor que cero.")
    if Nf < N0:
        raise ValueError("Nf debe ser mayor que N0 para crecimiento.")

    # Función objetivo: queremos f(t) = 0
    def f(t):
        return N0 * (2 ** (t / t_dup)) - Nf

    # Intervalo inicial para la bisección
    # t no puede ser negativo, y un límite superior razonable es
    # el número de duplicaciones necesarias multiplicado por t_dup.
    # Para estar seguros, ponemos un margen grande.
    t_low = 0
    t_high = t_dup * 100  # margen amplio para garantizar que cubre la solución

    # Búsqueda por bisección
    for _ in range(200):  # iteraciones suficientes para buena precisión
        t_mid = (t_low + t_high) / 2
        if f(t_mid) == 0:
            return t_mid
        elif f(t_mid) > 0:
            t_high = t_mid
        else:
            t_low = t_mid

    return (t_low + t_high) / 2

levaduras_TiempoParaAlcanzarN(1000, 10000000)