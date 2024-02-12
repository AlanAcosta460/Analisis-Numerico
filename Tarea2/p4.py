import numpy as np
import matplotlib.pyplot as plt

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
    return np.exp(x)

print("%%%%% Bienvenido al programa %%%%%")
print("\n*** Dibujo de funcion f(x) ***")

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

    plt.figure(figsize = (10, 6))
    plt.axhline(0, color = "black", linewidth = 1) 
    plt.axvline(0, color = "black", linewidth = 1) 

    if opcion == 1 :
        valores = np.linspace(-5, 5, 400)
        plt.plot(valores, fx1(valores), label = "2x + 1")
    elif opcion == 2 :
        valores = np.linspace(-6, 4, 400)
        plt.plot(valores, fx2(valores), label = "x^2 + 2x + 1")
    else :
        valores = np.linspace(-2, 10, 400)
        plt.plot(valores, fx3(valores), label = "e^x")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Funcion f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

    print("\n\nDesea volver a dibujar una funcion? (Si/No)")
    respuesta = input("$ ")
    respuesta.lower()

    if respuesta == "no" :
        break

print("\n\n%%%%%% Gracias por usar el programa %%%%%")
