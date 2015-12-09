
def anonymous(x):
	return x**2 + 1

def integrate_upper_bound(fun, start, end):
	step = 0.1
	intercept = start
	area = 0
	while end - intercept > step:
	'''
   		the original condition will encounter precision problem caused by 0.1
		python is using float as the default floating point number datatype
		a work-around solution is to introduce the concept of "delta" instead
		(i.e., the step size here) which indicate how close $end and $intercept
		are. 
	'''
		intercept += step 
		area += step*fun(intercept)

	return area

def integrate_lower_bound(fun, start, end):
	step = 0.1
	intercept = start
	area = 0
	while end - intercept > step:
		area += step*fun(intercept)
		intercept += step

	return area

if __name__ == '__main__':
	print('upper bound: '+str(integrate_upper_bound(anonymous, 0, 10)))
	print('lower bound: '+str(integrate_lower_bound(anonymous, 0, 10)))
