def dobro(i):
	return i*2

x = [1,2,3,4,5,6]

dobrado  = map(dobro,x)
dobrado = list(dobrado)
for v in dobrado:
	print(v)
