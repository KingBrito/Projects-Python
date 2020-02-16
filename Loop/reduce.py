from functools import reduce
def soma(x,y):
	return x+y

x = [45,87,54,8,6,544,74,65]

soma = reduce(soma,x)

print(soma)
