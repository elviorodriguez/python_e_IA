def A():
	print("Dentro de A")
def B(y):
	print("Dentro de B")
	return y
def C(z):
	print("Dentro de C")
	return z(2)

print( A() )
print( 3 + B(y = 2) )
print( C(B) )

