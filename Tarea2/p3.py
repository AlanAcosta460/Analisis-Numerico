import numpy as np

def menu() :
    print("\n*** MENU ***")
    print("1) f(x) = 2x + 1")
    print("2) f(x) = x^2 + 2x + 1")
    print("3) f(x) = e^x")

def fx1(x) :
    return (2 * x) + 1

def fx2(x) :
    return (x * x) + (2 * x) + 1

def fx3(x) :
    return round(np.exp(x), 2)

print("%%%%% Bienvenido al programa %%%%%")
print("\n*** Tabulacion de funcion f(x) ***")

while True :
    
    menu()
    while True :
        print("\nPor favor seleccion una opcion")
        opcion = int(input("$ "))

        if opcion < 1 or opcion > 4 :
            print("\n\t\t*** Opcion invalida ***\n")
            continue
        else :
            break
    
    print("\n*** Resultados ***")
    print("f(x)\tx")

    for x in range(11) :
        if opcion == 1 :
            calculo = fx1(x) 
        elif opcion == 2 :
            calculo = fx2(x) 
        else :
            calculo = fx3(x) 
            
        print(f"{x}\t{calculo}")

    print("\n\nDesea volver a tabular una funcion? (Si/No)")
    respuesta = input("$ ")
    respuesta.lower()

    if respuesta == "no" :
        break

print("\n\n%%%%%% Gracias por usar el programa %%%%%")
