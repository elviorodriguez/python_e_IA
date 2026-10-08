# INPUT
x = float(input("Ingrese un Nº para x: "))
y = float(input("Ingrese un Nº para y: "))

# Control de flujo ramifcado
if x == y:
    print("x e y son iguales")

    # evitamos un error de división por 0
    if x != 0:
        print("Por lo tanto x/y =", x/y)        

elif x < y:
    print("x es menor")

else:
    print("y es mayor")


print('')
print('Fin del código!')
