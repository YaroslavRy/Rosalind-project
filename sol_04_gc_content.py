my_path = "C:/Users/nemoSys/Downloads/tmp/rosalind_gc.txt"

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
        cg_counter = 0
        for i in cur_dna_block:
            if i == "C" or i == "G":
                cg_counter += 1
        gc_content_value = cg_counter / len(cur_dna_block) * 100
        gc_content_value = round(gc_content_value, round_digits)
        gc_content_result[block_id] = gc_content_value
    max_block_id = max(gc_content_result, key=gc_content_result.get)
    print(max_block_id)
    print(gc_content_result[max_block_id])
    
data = parse_data(path_to_file)
calc_gc_content(data)

