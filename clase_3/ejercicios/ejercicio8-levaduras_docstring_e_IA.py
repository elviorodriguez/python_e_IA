# -*- coding: utf-8 -*-

def levaduras_TiempoParaAlcanzarN(N0, Nf, t_dup = 2):
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