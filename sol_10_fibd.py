# coding: utf-8


'''
Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100n≤100 and m≤20m≤20.

Return: The total number of pairs of rabbits that will remain after the nn-th
month if all rabbits live for mm months. 

Sample Dataset
6 3

Sample Output
4
'''


import os


def read_data(path):
	if path == None:
		r = '''6 3'''
	else:
		f = open(path)
		r = f.read()
	s = r.split()
	s = [int(i) for i in s]
	return s	


def fibd(n, k=3):
	# n month road
	# k month rabbit`s lifetime 

	ages = [1] + [0]*(k-1)
	for i in range(n-1):
		ages = [sum(ages[1:])] + ages[:-1]
	print(sum(ages))


if __name__ == '__main__':
	path_to_file = os.path.join(os.path.dirname(__file__), 'data/rosalind_fibd.txt')
	n, k = read_data(path_to_file)
	fibd(n, k)
