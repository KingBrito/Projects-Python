def impar(i):
	if i%2 == 1:
		return i

lista = [1,2,3,4,5,6,7,8,9,10]

listaimpar = filter(impar,lista)
print(list(listaimpar))
