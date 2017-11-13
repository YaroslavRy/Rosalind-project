path_to_file = "C:/Users/nemoSys/Downloads/tmp/rosalind_hamm.txt"

def calc_hamming_distance(path_to_file):
    if path_to_file == None:
        file = """GAGCCTACTAACGGGAT
                  CATCGTAATGACGGCCT"""
    else:
        file = open(path_to_file).read()
    seqences = file.split()
    seq1 = seqences[0]
    seq2 = seqences[1]
    diff_counter = 0
    for i in range(len(seq1)):
        res = seq1[i] == seq2[i]
        if res == False:
            diff_counter += 1
    return diff_counter

calc_hamming_distance(path_to_file)