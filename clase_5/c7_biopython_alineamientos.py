# -*- coding: utf-8 -*-

from Bio.Seq import Seq
from Bio.Align import PairwiseAligner

seq1 = Seq("ATGCTAGCTAG")
seq2 = Seq("CAAATGCGAGCTAGCC")

######################################
# ------ Alineamiento global ------- #
######################################

# Cargar el alineador en modo global
aligner = PairwiseAligner()
aligner.mode = "global"

# Alinear
alignments = aligner.align(seq1, seq2)

# Ver alineamiento y score
print(alignments[0])
print("Score:", alignments[0].score)

######################################
# ------ Alineamiento global ------- #
######################################

# Cargar el alineador en modo local
aligner = PairwiseAligner()
aligner.mode = "local"

# Alinear
alignments = aligner.align(seq1, seq2)

# Alinear
print(alignments[0])
print("Score:", alignments[0].score)