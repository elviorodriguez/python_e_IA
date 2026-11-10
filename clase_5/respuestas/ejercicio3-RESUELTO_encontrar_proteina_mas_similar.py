# -*- coding: utf-8 -*-

'''
EJERCICIO 3 - Clase 5:
    
Crear un programa que permita encontrar cual es la proteína humana más parecida
a Q08649 de S. cerevisiae utilizando los módulos/clases de Biopython Seq, SeqIO
y Align/PairwiseAligner. El programa debe cargar la base de datos utilizando
SeqIO y luego comparar la secuencia de interés (Q08649) con cada una de las
proteínas de la base de datos de proteínas humanas "ejercicio3_base_de_datos.fasta".
¿El alineamiento global da el mismo resultado que el alineamiento local?

Utilizar ChatGPT, Claude, Gemini o Copilot como asistente de generación de 
código para resolver el ejercicio.

Recomendación: mostrarle los ejemplos de código de clase (c5, c6 y c7).
'''

# Importar módulos de Biopython
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices


# ------------------------------------------------
# 1. Secuencia de interés
# ------------------------------------------------

# Uniprot ID Q08649 - Esa1 de S. cerevisiae

secuencia_de_interes = Seq(
    "MSHDGKEEPGIAKKINSVDDIIIKCQCWVQKNDEERLAEILSINTRKAPPKFYVHYVNYNKRLDEWITTDRINLDKEVLYPKLKATDEDNKKQKKKKATNTSETPQDSLQDGVDGFSRENTDVMDLDNLNVQGIKDENISHEDEIKKLRTSGSMTQNPHEVARVRNLNRIIMGKYEIEPWYFSPYPIELTDEDFIYIDDFTLQYFGSKKQYERYRKKCTLRHPPGNEIYRDDYVSFFEIDGRKQRTWCRNLCLLSKLFLDHKTLYYDVDPFLFYCMTRRDELGHHLVGYFSKEKESADGYNVACILTLPQYQRMGYGKLLIEFSYELSKKENKVGSPEKPLSDLGLLSYRAYWSDTLITLLVEHQKEITIDEISSMTSMTTTDILHTAKTLNILRYYKGQHIIFLNEDILDRYNRLKAKKRRTIDPNRLIWKPPVFTASQLRFAW"
)


# ------------------------------------------------
# 2. Cargar la base de datos de proteínas humanas
# ------------------------------------------------

base_de_datos_fasta = "ejercicio3_base_de_datos.fasta"

# Leer el archivo FASTA utilizando SeqIO
registros = list(SeqIO.parse(base_de_datos_fasta, "fasta"))

print("Cantidad de proteínas cargadas:", len(registros))


# ------------------------------------------------
# 3. Función para buscar la proteína más parecida
# ------------------------------------------------

def encontrar_mejor_alineamiento(secuencia, registros, modo):

    # Crear el alineador
    aligner = PairwiseAligner()

    # Seleccionar el tipo de alineamiento
    aligner.mode = modo

    # Utilizar una matriz de sustitución para proteínas
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")

    # Establecer penalizaciones por gaps
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5

    # Inicializar el mejor resultado
    mejor_score = float("-inf")
    mejor_proteina = None
    mejor_alineamiento = None

    # Comparar la secuencia de interés con cada proteína
    for registro in registros:

        alineamientos = aligner.align(secuencia, registro.seq)

        # Obtener el mejor alineamiento de esa comparación
        alineamiento = alineamientos[0]

        # Comparar el score con el mejor obtenido hasta el momento
        if alineamiento.score > mejor_score:

            mejor_score = alineamiento.score
            mejor_proteina = registro
            mejor_alineamiento = alineamiento

    return mejor_proteina, mejor_alineamiento, mejor_score


# ------------------------------------------------
# 4. ALINEAMIENTO GLOBAL
# ------------------------------------------------

print("\n===================================")
print("       ALINEAMIENTO GLOBAL")
print("===================================")

mejor_global, alineamiento_global, score_global = encontrar_mejor_alineamiento(
    secuencia_de_interes,
    registros,
    "global"
)

print("Proteína humana más parecida:")
print("ID:", mejor_global.id)
print("Descripción:", mejor_global.description)
print("Score:", score_global)

print("\nAlineamiento:")
print(alineamiento_global)


# ------------------------------------------------
# 5. ALINEAMIENTO LOCAL
# ------------------------------------------------

print("\n===================================")
print("        ALINEAMIENTO LOCAL")
print("===================================")

mejor_local, alineamiento_local, score_local = encontrar_mejor_alineamiento(
    secuencia_de_interes,
    registros,
    "local"
)

print("Proteína humana más parecida:")
print("ID:", mejor_local.id)
print("Descripción:", mejor_local.description)
print("Score:", score_local)

print("\nAlineamiento:")
print(alineamiento_local)


# ------------------------------------------------
# 6. Comparar los resultados
# ------------------------------------------------

print("\n===================================")
print("       COMPARACIÓN FINAL")
print("===================================")

if mejor_global.id == mejor_local.id:

    print("El alineamiento global y el local dieron el mismo resultado.")

    print("Proteína encontrada:", mejor_global.id)

else:

    print("El alineamiento global y el local dieron resultados diferentes.")

    print("Mejor proteína (Global):", mejor_global.id)
    print("Mejor proteína (Local):", mejor_local.id)
