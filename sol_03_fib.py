'''
Given: Positive integers n≤40n≤40 and k≤5k≤5.

Return: The total number of rabbit pairs that will be present after nn months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of kk rabbit pairs (instead of only 1 pair).

Sample Dataset
5 3

Sample Output
19
'''


import os

def read_data(path):
	if path == None:
		r = '''5 3'''
	else:
		f = open(path)
		r = f.read()
	s = r.split()
	s = [int(i) for i in s]
	return s	


def fib(s):
	n, k = s[0], s[1]
	a, b = 1, 1
	for i in range(n-1):
		a, b = b, b + (a * k)
	return a


if __name__ == '__main__':
	path_to_file = os.path.join(os.path.dirname(__file__), 'data/rosalind_fib.txt')
	data = read_data(path=path_to_file)
	res = fib(data)
	print(res)