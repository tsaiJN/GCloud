
def anonymous(x):
	return x**2 + 1

def integrate(fun, start, end):
	step = 0.1
	intercept = start
	area = 0
	while intercept < end:
		intercept += step # above curve version: 358.651
		''' my work '''
		area += step*fun(intercept)
#		intercept += step # under curve version: 348.45

	return area

if __name__ == '__main__':
	print(integrate(anonymous, 0, 10))
