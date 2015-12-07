import numpy as np


def recursive_comb(n, r):
	if r == 1:
		return n
	if r == n:
		return 1

	return recursive_comb(n-1, r) + recursive_comb(n-1, r-1)

def DP_comb(n, r):
	DP_table = np.empty([1000, 1000])
	for i in range(n+1):
		DP_table[i][1] = i
	for i in range(n+1):
		DP_table[i][i] = 1

	for i in range(2, n+1):
		for j in range(2, i+1):
			DP_table[i][j] = DP_table[i-1][j-1] + DP_table[i-1][j]
	return DP_table[n][r]
	


def demo(n, r):
#	print( 'C('+str(n)+', '+str(r)+') = '+str(recursive_comb(n, r))+'.\n')   # time consumming
	print( 'C('+str(n)+', '+str(r)+') = '+str(DP_comb(n, r))+'.\n')

if __name__ == '__main__':
	demo(40, 10)
	demo(990, 33)
