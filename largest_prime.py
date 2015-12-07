

def largest_prime(n):
	""" finding all the prime factors and return the max one """
	factors = set()
	base = 2
	while n > 1:
		while n % base == 0:
			factors.add(base)
			n /= base
		base += 1

	return max(factors)


def demo(n):
	print('largest prime of '+str(n)+' is '+str(largest_prime(n))+'.\n')


if __name__ == '__main__':
	demo(13195)
	demo(600851475143)
