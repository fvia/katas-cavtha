#!/usr/bin/env python 
import sys

def AreaTriangulo(base, altura):
    return base * altura / 2


def AreaRectangulo(base, altura):
    return base * altura


def AreaCuadrado(lado):
    return lado * lado


def uso():
    print( 
"""USO: Calcula el area de la figura indicada
areas cuadrado <lado>
areas rectangulo <base> <altura>
areas triangilo <base> <altura> 
p.e.   areas cuadrado 5""")


def sal_con_error(mensaje):
    print(mensaje)
    uso()
    exit(1)


def num(n):
    "returns num or None"
    try:
        return float(n)
    except:
        return None  	

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sal_con_error("areas: numero de argumentos insuficiente")
    
    if sys.argv[1].lower() == "cuadrado":
        if len(sys.argv) != 3:
             sal_con_error('numero de argumentos erroneo')
        if num(sys.argv[2])!=None:
             print( AreaCuadrado(num(sys.argv[2]))) 
             exit(0)

    sal_con_error("Error Indeterminado")

