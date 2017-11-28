from Bio import motifs
from Bio.Seq import Seq
import os


def read_data(path):
	if path == None:
		r = '''>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT'''
	else:
		f = open(path)
		r = f.read()
		f.close()
	data = r.split('>')
	result = {}
	for i in data:
		if len(i) > 0:
			block = i.strip().split()
			block_id = block[0]
			seq = ''.join(block[1:])
			result[block_id] = seq
	return result


def get_consenus(data):
	inst = []
	for i in data:
		inst.append(Seq(data[i]))
	m = motifs.create(inst)
	count_matrix = m.counts
	for key, value in count_matrix.items():
		return "".join(key + ': ' + ' '.join(map(str, value)))


if __name__ == '__main__':
	path_to_file = os.path.join(os.path.dirname(__file__), 'data/rosalind_cons.txt')
	data = read_data(path=path_to_file)
	result = get_consenus(data)
	print(result)

