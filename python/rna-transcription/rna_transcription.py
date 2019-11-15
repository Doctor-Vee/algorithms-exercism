def to_rna(dna_strand):
    rna_strand = ""
    for i in dna_strand:
        if i == "A":
            rna_strand += "U"
        if i == "C":
            rna_strand += "G"
        if i == "G":
            rna_strand += "C"
        if i == "T":
            rna_strand += "A"
    return rna_strand

# # From Community solutions
# def to_rna(dna_strand):
#     transcription = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
#     return ''.join([transcription[nuc] for nuc in dna_strand])