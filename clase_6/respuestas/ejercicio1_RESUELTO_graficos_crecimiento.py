# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

###############################################################################
# --------------------------------- INPUT ----------------------------------- #
###############################################################################

# Valores de X
dias = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14]

# ----------------- Crecimiento de cepa con gen wild type (WT) ----------------

# Valores de Y1 (replicas sin inducir: control)
parasitos_genWT_ctrl_repA = [1.0, 2.4, 6.0, 11.2, 17.2, 23.4, 40.8, 53.0, 63.7, 64.0, 78.4, 88.0, 90.4]
parasitos_genWT_ctrl_repB = [1.0, 2.2, 5.2, 9.2, 15.4, 24.0, 35.1, 53.5, 61.6, 64.8, 64.0, 88.0, 88.0]
parasitos_genWT_ctrl_repC = [1.0, 2.6, 5.4, 10.4, 15.0, 24.2, 34.5, 50.5, 59.5, 64.8, 68.8, 77.6, 86.4]

# Valores de Y2 (réplicas sobreexpresante)
parasitos_genWT_sobreexp_repA = [1.0, 1.4, 2.2, 4.2, 5.2, 6.6, 9.0, 12.9, 20.1, 27.0, 40.0, 56.8, 62.4]
parasitos_genWT_sobreexp_repB = [1.0, 1.4, 2.4, 4.2, 4.6, 7.6, 8.4, 13.8, 20.4, 27.9, 41.0, 60.8, 62.4]
parasitos_genWT_sobreexp_repC = [1.0, 1.4, 2.6, 4.0, 5.2, 7.6, 9.3, 15.0, 20.1, 27.3, 38.5, 56.0, 64.8]


###############################################################################
# ------------------------------- CALCULOS ---------------------------------- #
###############################################################################
# Calculos acá

# Promedio en cada índice
parasitos_genWT_ctrl_promedio = [(a+b+c)/3 for a,b,c in zip(parasitos_genWT_ctrl_repA, parasitos_genWT_ctrl_repB, parasitos_genWT_ctrl_repC)]
parasitos_genWT_sobreexp_promedio = [(a+b+c)/3 for a,b,c in zip(parasitos_genWT_sobreexp_repA, parasitos_genWT_sobreexp_repB, parasitos_genWT_sobreexp_repC)]


###############################################################################
# ------------------------------- GRÁFICOS ---------------------------------- #
###############################################################################
# Gráficos acá

plt.figure("gen wt")
plt.clf()
plt.plot(dias, parasitos_genWT_ctrl_promedio, "g-", label = "WT control")
plt.plot(dias, parasitos_genWT_ctrl_repA, "go")
plt.plot(dias, parasitos_genWT_ctrl_repB, "go")
plt.plot(dias, parasitos_genWT_ctrl_repC, "go")
plt.plot(dias, parasitos_genWT_sobreexp_promedio, "r-", label = "WT sobreexpresante")
plt.plot(dias, parasitos_genWT_sobreexp_repA, "ro")
plt.plot(dias, parasitos_genWT_sobreexp_repB, "ro")
plt.plot(dias, parasitos_genWT_sobreexp_repC, "ro")
plt.xlabel("Tiempo (d)")
plt.ylabel("Parásitos (mill/ml)")
plt.title("Cepa con gen Wild Type (WT)")
plt.legend()