'''
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Sample Dataset
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
Sample Output
Rosalind_0808
60.919540
'''


import os


def parse_data(path_to_file=None):
    if path_to_file == None:
        file = '''>Rosalind_6404
                CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
                TCCCACTAATAATTCTGAGG
                >Rosalind_5959
                CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
                ATATCCATTTGTCAGCAGACACGC
                >Rosalind_0808
                CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
                TGGGAACCTGCGGGCAGTAGGTGGAAT'''
            
    else:
        file = open(path_to_file).read()
    data = file.split(">")
    res = {}
    for i in data:
        if len(i) > 0:
            block = i.strip().split()
            block_id = block[0]
            dna_seq = "".join(block[1:])
            res[block_id] = dna_seq
    return res

def calc_gc_content(data, round_digits=6):
    gc_content_result = {}
    for block_id in data:
        cur_dna_block = data[block_id]
        cg_counter = 0.0
        for i in cur_dna_block:
            if i == "C" or i == "G":
                cg_counter += 1
        gc_content_value = (cg_counter) / len(cur_dna_block) * 100
        gc_content_value = round(gc_content_value, round_digits)
        gc_content_result[block_id] = gc_content_value
    max_block_id = max(gc_content_result, key=gc_content_result.get)
    print(max_block_id)
    print(gc_content_result[max_block_id])


if __name__ == '__main__':
    path_to_file = os.path.join(os.path.dirname(__file__), 'data/rosalind_gc.txt')
    data = parse_data(path_to_file)
    calc_gc_content(data)


