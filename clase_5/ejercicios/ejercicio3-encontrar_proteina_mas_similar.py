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

from Bio import Seq

# Uniprot ID Q08649 - Esa1 (Histona Acetyl-transferasa Esa1 de S. cerevisiae)
secuencia_de_interes = Seq("MSHDGKEEPGIAKKINSVDDIIIKCQCWVQKNDEERLAEILSINTRKAPPKFYVHYVNYNKRLDEWITTDRINLDKEVLYPKLKATDEDNKKQKKKKATNTSETPQDSLQDGVDGFSRENTDVMDLDNLNVQGIKDENISHEDEIKKLRTSGSMTQNPHEVARVRNLNRIIMGKYEIEPWYFSPYPIELTDEDFIYIDDFTLQYFGSKKQYERYRKKCTLRHPPGNEIYRDDYVSFFEIDGRKQRTWCRNLCLLSKLFLDHKTLYYDVDPFLFYCMTRRDELGHHLVGYFSKEKESADGYNVACILTLPQYQRMGYGKLLIEFSYELSKKENKVGSPEKPLSDLGLLSYRAYWSDTLITLLVEHQKEITIDEISSMTSMTTTDILHTAKTLNILRYYKGQHIIFLNEDILDRYNRLKAKKRRTIDPNRLIWKPPVFTASQLRFAW")

# Este archivo tiene todas las proteínas para buscar la más similar
base_de_datos_fasta = "ejercicio3_base_de_datos.fasta"