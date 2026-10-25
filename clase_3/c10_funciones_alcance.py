def maxPlus(x, y):
	if x > y:
		x = x + 1000
		return x
	else:
		y = y + 1000
		return y
x = 4
y = 3
resultado = maxPlus(x = y, y = x)
print("Resultado =", resultado)
print("x =", x)
print("y =", y)
