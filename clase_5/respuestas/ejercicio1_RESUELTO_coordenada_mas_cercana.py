# -*- coding: utf-8 -*-

class Coordenada(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distancia(self, other):
        delta_x_cuadrado = (self.x - other.x) ** 2
        delta_y_cuadrado = (self.y - other.y) ** 2
        return (delta_x_cuadrado + delta_y_cuadrado) ** 0.5
    
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    
    def __sub__(self, other):
        return Coordenada(self.x - other.x, self.y - other.y)
    
    def encontrar_mas_cercana(self, others):    # <---------------- COMPLETAR
        '''
        Encuenta la coordenada más cercana y la devuelve.

        Parameters
        ----------
        others : list[Coordenadas]
            Lista de objetos de clase Coordenada.

        Returns
        -------
        Coordenada
            Coordenada más cercana a self.
        '''
        
        # Inicializamos con la primer coordenada
        coord_mas_cercana = others[0]
        distancia_mas_cercana = self.distancia(others[0])
        
        for coord in others[1:]:
            
            distancia = self.distancia(coord)
            
            if self.distancia(coord) < distancia_mas_cercana:
                coord_mas_cercana = coord
                distancia_mas_cercana = distancia
        
        return coord_mas_cercana
            
        

# Crear las instancias de tipo Coordenada
c1 = Coordenada(10,5)
c2 = Coordenada(12,-520)
c3 = Coordenada(120,-12)
c4 = Coordenada(325,104)
c5 = Coordenada(-50,-75)

# Ver cual es la más cercana
lista_de_coordenadas = [c2, c3, c4, c5]
print(c1.encontrar_mas_cercana([lista_de_coordenadas]))

