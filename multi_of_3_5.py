

def sum_of_mult_3_5(n):

	mult_amt_3 = n/3
	mult_amt_5 = n/5
	mult_amt_15 = n/15

	return cumulate(mult_amt_3)*3 + cumulate(mult_amt_5)*5 - cumulate(mult_amt_15)*15
	
def cumulate(n):
	""" cumulate number from 1 to n, that is 1+2+3+...+n """
	sum = 0;
	for i in range(n+1):
		sum += i

	return sum

def demo(n):
	print( 'Multiples of 3 and 5 below '+str(n)+' is '+str(sum_of_mult_3_5(n))+'.\n')

if __name__ == '__main__':
	demo(10-1)	# Ooops I misunderstood "below" as including the given value/ However, this will work :p
	demo(1000-1)
