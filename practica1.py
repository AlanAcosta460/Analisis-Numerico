import math

# Variables Globales
r = 0 
v = 0 
valores = {}

def presentacion() :
    print("****************************************************")
    print("\n\t\t ANÁLISIS NUMÉRICO")
    print("\t\t      GRUPO: 4")
    print("\t\tMÉTODO DE BISECCIÓN\n")
    print("****************************************************")

    print("\n\n*** Integrantes del equipo ***")
    print("- Acosta Porcayo Alan Omar")
    print("- Alvarez González Eduardo")
    print("- Hernández Castillo Rubén")

def menu() :
    print("\n*** MENU ***")
    print("1. Obtener las raices de sin(x) - cosec(x) + 1 = 0")
    print("2. Obtener h en V = (πh^2(3r - h)) / 3")

    while True :
        op = int(input("$ "))
        if op < 1 or op > 2 :
            print("\n\tValor invalido\n")
        else :
            break
    return op

def funcion1(x) :
    return math.sin(x) - (1 / math.sin(x)) + 1 

def funcion2(h) :
    return pow(h, 3) - (3 * r * pow(h, 2)) + ((3 * v) / math.pi)

def tabular() :
    print("***** Tabulacion *****")
    print("x\tf(x)")
    
    for valor in valores : 
        print(f"{valor}\t{valores[valor]}")
    
def biseccion(op) :
    print("\n*** Biseccion ***")
    
    while True :
        print("Dame el valor de xI")
        xI = float(input("$ "))

        print("Dame el valor de xS")
        xS = float(input("$ "))
        
        if op == 1 :
            fxI = funcion1(xI)
            fxS = funcion1(xS)
        else :
            fxI = funcion2(xI)
            fxS = funcion2(xS)

        if fxI * fxS >= 0 :
            print("\n\tIntervalo invalido \n")
        else :
            break

    tol = 0.01
    print(f"\n*** La tolerancia es de {tol} ***\n") 
    print("\nIteracion\txI\txP\txS\tf(xI)\tf(xP)\tf(xS)\t|xS - xI|\t|xS - xI| <= tol")
    it = 1
    while True :
        if op == 1 :
            fxI = round(funcion1(xI), 3)
            fxS = round(funcion1(xS), 3)
        else :
            fxI = round(funcion2(xI), 3)
            fxS = round(funcion2(xS), 3)
        
        xP = round((xI + xS) / 2, 3)

        if op == 1 : 
            fxP = round(funcion1(xP), 3)
        else :
            fxP = round(funcion2(xP), 3)

        dif = round(abs(xS - xI), 3)

        print(f"{it}\t\t{xI}\t{xP}\t{xS}\t{fxI}\t{fxP}\t{fxS}\t{dif}\t\t{dif <= tol}")

        if (fxI * fxP) < 0 :
            xS = xP
        elif (fxI * fxP) > 0 : 
            xI = xP

        if (fxI * fxP) == 0 or dif <= tol :
            break 
        
        it += 1

    print(f"\n **** La raiz es {xP} ****\n\n")
    
def main() :
    presentacion()
    
    print()
    while True :
        op = menu()

        valores.clear()
        if op == 1 :
            x = 0.1
            for i in range(0, 50) :
                valores[round(x, 1)] = round(funcion1(x), 3)
                x += 0.1
        elif op == 2 :
            global r, v

            print("\nDame el valor de r en metros")
            r = float(input ("$ "))
            print("Dame el valor de V en metros cubicos")
            v = float(input("$ "))

            h = 0.0
            for i in range(0, 50) :
                valores[round(h, 1)] = round(funcion2(h), 3)
                h += 0.2


        print()
        tabular()

        biseccion(op)

        print("Desear realizar otro calculo? (s/n)")
        repetir = input("$ ")
    
        if repetir != "s" :
            break
    
    print("\nGRACIAS POR USAR EL PROGRAMA!!!")


if __name__ == "__main__":
    main()
