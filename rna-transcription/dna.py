#python 3.5 version

def to_rna(sequence):
    return sequence.translate(str.maketrans("GCTA","CGAU"))
