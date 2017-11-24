'''
Given two strings ss and tt, tt is a substring of ss if tt is contained as a contiguous collection of symbols in ss (as a result, tt must be no longer than ss).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position ii of ss is denoted by s[i]s[i].

A substring of ss can be represented as s[j:k]s[j:k], where jj and kk represent the starting and ending positions of the substring in ss; for example, if ss = "AUGCUUCAGAAAGGUCUUACG", then s[2:5]s[2:5] = "UGCU".

The location of a substring s[j:k]s[j:k] is its beginning position jj; note that tt will have multiple locations in ss if it occurs more than once as a substring of ss (see the Sample below).

Given: Two DNA strings ss and tt (each of length at most 1 kbp).

Return: All locations of tt as a substring of ss.

Sample Dataset
GATATATGCATATACTT
ATAT

Sample Output
2 4 10
'''

import os

def read_data(path):
	if path == None:
		r = '''GATATATGCATATACTT
		ATAT'''
	else:
		f = open(path)
		r = f.read()
	s, t = r.split()
	return s, t

def get_locations(s, t):
	len_s = len(s)
	len_t = len(t)
	 
	locations = [] 
	for i in range(len_s - 1):
		if s[i:i+len_t] == t:
			locations.append(i+1)
	return locations

if __name__ == '__main__':
	path_to_file = os.path.join(os.path.dirname(__file__), 'data/rosalind_subs.txt')
	s, t = read_data(path_to_file)
	locations = get_locations(s, t)
	locations_str = ' '.join(map(str, locations))
	print(locations_str)
