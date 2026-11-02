# -*- coding: utf-8 -*-

# Definición del dict
info_proteinas = {'P59021' : ('MTGRAAT', 9.5),
                  'P55322' : ('MYRGPPS', 8.5),
                  'P63243' : ('MLLVLIT', 5.3)}

# Recuperar info del dict
info_proteinas['P55322']

# Agregar información a los dict (mutar)
print(info_proteinas)
nuevo_ID = 'P99298'
nuevos_datos = ('MRRRRRR', 12.7)
info_proteinas[nuevo_ID] = nuevos_datos
print(info_proteinas)

# Borrar información
del(info_proteinas['P59021'])