def get_hamming_distance(dna1, dna2):
    distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1
    return distance


def get_dna_complement(dna):
    complement = ""
    for base in dna:
        if base == 'A':
            complement = 'T' + complement
        elif base == 'T':
            complement = 'A' + complement
        elif base == 'C':
            complement = 'G' + complement
        elif base == 'G':
            complement = 'C' + complement
    return complement
