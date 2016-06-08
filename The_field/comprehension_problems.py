def my_filter(L,n):
	return [x for x in L if x % n == 0]


def my_list(L):
	return [[y for y in range(1, x+1)] for x in L  ]


def my_function_composition(f,g):
	return { k:g[f[k]] for k in f.keys()}
 
print "Problem 1.7.1"
print my_filter([1,2,3,4,5,6],2)
print "Problem 1.7.2"
print my_list([1,2,4])
print "Problem 1.7.3"
print my_function_composition({0:'a',1:'b'},{'a':'apple','b':'banana'})
