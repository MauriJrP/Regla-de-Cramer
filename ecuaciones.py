import os

#--------Funcion para resolver sistemas de ecuaciones 2x2---------
def solucion_sistema_2x2(a1,a2,b1,b2,c1,c2):
    delta = (a1 * b2) - (a2 * b1)
    if delta != 0:
        x = ( c1 * b2 - c2 * b1 ) / delta
        y = ( a1 * c2 - a2 * c1 ) / delta
        return x, y
    else: 
        print("El sistema no tiene una solucion unica...")

#--------Funcion para resolver sistemas de ecuaciones 3x3---------
def solucion_sistema_3x3(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    delta = (a1)

#-----------------------------------MENU---------------------------------------------------
def main():
    datos = []
    i = 0
    print("1.- Sistema 2x2\n2.-Sistema 3x3")
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        print("Sistema de 2 ecuaciones lineales con 2 incongnitas")
        print("Estructura:\na1x + b1y = c1\na2x + b2y = c2\n\nIngesa los datos:")
        a1 = int(input("a1 = "))
        b1 = int(input("b1 = "))
        c1 = int(input("c1 = "))
        a2 = int(input("a2 = "))
        b2 = int(input("b2 = "))
        c2 = int(input("c2 = "))
        x,y = solucion_sistema_2x2(a1,a2,b1,b2,c1,c2);
        print("\nSolucion: \nx = ",x,"\ny = ",y)
    elif opcion == 2:
        print("Sistema de 3 ecuaciones lineales con 3 incognitas")
        print("Estructura:\na1x + b1y + c1z = d1\na2x + b2y + c2z = d2\na3x + b3y + c3z = d3")
        a1 = int(input("a1 = "))
        b1 = int(input("b1 = "))
        c1 = int(input("c1 = "))
        c1 = int(input("d1 = "))
        a2 = int(input("a2 = "))
        b2 = int(input("b2 = "))
        c2 = int(input("c2 = "))
        c2 = int(input("d2 = "))
        a3 = int(input("a3 = "))
        b3 = int(input("b3 = "))
        c3 = int(input("c3 = "))
        c3 = int(input("d3 = "))
        x,y,z = solucion_sistema_2x2(a1,a2,b1,b2,c1,c2);
        print("\nSolucion: \nx = ",x,"\ny = ",y,"\nz = ")
main();
