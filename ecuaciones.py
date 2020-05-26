import os
from time import sleep

#--------Funcion para resolver sistemas de ecuaciones 2x2---------
def solucion_sistema_2x2(a1,a2,b1,b2,c1,c2):
    x,y = False, False
    delta = (a1 * b2) - (a2 * b1)
    if delta != 0:
        x = ( c1 * b2 - c2 * b1 ) / delta
        y = ( a1 * c2 - a2 * c1 ) / delta
    else: 
        print("El sistema no tiene una solucion unica...")
    return x, y

#--------Funcion para resolver sistemas de ecuaciones 3x3---------
def solucion_sistema_3x3(a1,a2,a3,b1,b2,b3,c1,c2,c3,d1,d2,d3):
    x,y,z = False, False, False
    positivo = 0; negativo = 0
    positivo = (a1 * b2 * c3) + (b1 * c2 * a3) + (c1 * a2 * b3)
    negativo = (-1 * a3 * b2 * c1) + (-1 * b3 * c2 * a1) + (-1 * c3 * a2 * b1)
    delta = positivo + negativo
    if delta != 0:
        positivo = (d1 * b2 * c3) + (b1 * c2 * d3) + (c1 * d2 * b3)
        negativo = (-1 * d3 * b2 * c1) + (-1 * b3 * c2 * d1) + (-1 * c3 * d2 * b1)
        x = (positivo + negativo) / delta
        positivo = (a1 * d2 * c3) + (d1 * c2 * a3) + (c1 * a2 * d3)
        negativo = (-1 * a3 * d2 * c1) + (-1 * d3 * c2 * a1) + (-1 * c3 * a2 * d1)
        y = (positivo + negativo) / delta
        positivo = (a1 * b2 * d3) + (b1 * d2 * a3) + (d1 * a2 * b3)
        negativo = (-1 * a3 * b2 * d1) + (-1 * b3 * d2 * a1) + (-1 * d3 * a2 * b1)
        z = (positivo + negativo) / delta
    else: 
        print("Delta es igual a 0, el sistema no tiene una solucion unica...")
    return x,y,z

#-----------------------------------MENU---------------------------------------------------
def main():
    try:
        opcion = 0
        while opcion != 3:
            os.system('cls')
            print("1.- Sistema 2x2\n2.-Sistema 3x3\n3.-Salir")
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
                x,y = solucion_sistema_2x2(a1,a2,b1,b2,c1,c2)
                if x: print("\nSolucion: \nx = ",x,"\ny = ",y)
            elif opcion == 2:
                print("\nSistema de 3 ecuaciones lineales con 3 incongnitas")
                print("Estructura:\na1x + b1y + c1z = d1\na2x + b2y + c2z = d2\na3x + b3y + c3z = d3\n")
                a1 = float(input("Ecuacion 1:\na1 = "))
                b1 = float(input("b1 = "))
                c1 = float(input("c1 = "))
                d1 = float(input("d1 = "))
                a2 = float(input("Ecuacion 2:\na2 = "))
                b2 = float(input("b2 = "))
                c2 = float(input("c2 = "))
                d2 = float(input("d2 = "))
                a3 = float(input("Ecuacion 3:\na3 = "))
                b3 = float(input("b3 = "))
                c3 = float(input("c3 = "))
                d3 = float(input("d3 = "))
                x,y,z = solucion_sistema_3x3(a1,a2,a3,b1,b2,b3,c1,c2,c3,d1,d2,d3)
                if x: print("\nSolucion: \nx = ",x,"\ny = ",y,"\nz = ",z)
            sleep(5)
    except:
        print("Solo Funciona con numeros reales... Intenta denuevo")
        main()
main()
