print("-----------------------------------")
print("------------prestamo---------------")
print("-----------------------------------")

#input

prestamo=int(input("ingrese el prestamo que quiere pedir:"))
deudas=int(input("ingrese su numero de deudas:"))
ingresos=int(input("ingrese susalario:"))


#prosecing

if deudas==0 and  ingresos>945200:
    print("puede sacar el prestamo")
elif deudas>0 and ingresos<945200:
    print("no puede sacar el prestamo")