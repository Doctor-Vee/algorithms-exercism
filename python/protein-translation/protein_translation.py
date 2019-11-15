def proteins(strand):
    codons = []
    protein = []
    i = 0
    while i<len(strand):
        codons.append(strand[i:i+3])
        i+=3
    
    for codon in codons:
        if codon == "AUG":
            protein.append("Methionine")
        if codon == "UUU" or codon == "UUC":
            protein.append("Phenylalanine")
        if codon == "UUA" or codon == "UUG":
            protein.append("Leucine")
        if codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG":
            protein.append("Serine")
        if codon == "UAU" or codon == "UAC":
            protein.append("Tyrosine")
        if codon == "UGU" or codon == "UGC":
            protein.append("Cysteine")
        if codon == "UGG":
            protein.append("Tryptophan")
        if codon == "UAA" or codon == "UAG" or codon == "UGA":
            return protein
    return protein