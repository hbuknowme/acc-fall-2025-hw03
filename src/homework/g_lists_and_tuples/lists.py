# Calculates p-distance between two DNA strings
def get_p_distance(list1, list2):
    differences = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            differences += 1
    return differences / len(list1)

# Builds the full p-distance matrix between multiple DNA strings
def get_p_distance_matrix(dna_lists):
    size = len(dna_lists)
    matrix = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            matrix[i][j] = round(get_p_distance(dna_lists[i], dna_lists[j]), 5)
    return matrix
