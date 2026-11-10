# -*- coding: utf-8 -*-

###############################################
########### DEFINICIÓN DE LA CLASE ############
###############################################

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

###############################################
########### UTILIZACIÓN DE LA CLASE ###########
###############################################

# Crear instancias de tipo Coordenada
c1 = Coordenada(3,4)
c2 = Coordenada(-3,2)
origen = Coordenada(0,0)

# Distancias 
c1.distancia(origen)
c1.distancia(c2)

# No se suele hacer así:
Coordenada.distancia(c1, origen)

# Print de los objetos
print(c1)


