from ast import If
from re import X
from tkinter.tix import Y_REGION


print("-------------------------------")
print("-calcular la pocicion de x y y-")
print("-------------------------------")

#input

X=int(input("ingrese la cordenada de x:"))

Y=int(input("ingrese la cordenada de y:"))

#prosecing

if X>0 and Y>0:
    print("el punto esta en el primer cuadrante")
elif X<0 and Y>0:
    print("el punto esta en el segundo cuadrante")
elif X>0 and Y<0:
    print("el punto esta enel tercer cuadrante")
elif X>0 and Y<0:
    print("el punto esta en el cuarto cuadrante")
elif X==0 and Y==0:
    print("el punto esta en el origen")


print(" gracias por usar el programa:)")