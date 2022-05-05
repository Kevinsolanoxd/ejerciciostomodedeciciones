print("-------------------------")
print("--------ganancia---------")
print("-------------------------")
#input
precio_costo=int(input("ingrese el precio de costo: "))

#prosessing
if precio_costo<3000:
    ganancia=precio_costo*0.15
else:
    if precio_costo<=6000:
        ganancia=500
    else:
        ganancia=precio_costo*0,25

venta= precio_costo + ganancia

#output
print(str(precio_costo) + " mas la ganancia que es " + str(ganancia) + " da " + str( venta ))
