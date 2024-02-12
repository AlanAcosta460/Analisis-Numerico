import numpy as np

print("%%%%% Bienvenido al programa %%%%%")
print("\n*** Mayor elemento de una Matriz ***")

while True :

    while True :
        print("\nPor favor ingrese el orden de la matriz")
        orden = int(input("$ "))

        if orden <= 0 :
            print("\n\t\t*** El numero debe ser positivo ***\n")
        else :
            break

    matriz = np.zeros((orden, orden))

    print("\n*** Ingrese los valores a continuacion ***")
    for i in range(orden):
        for j in range(orden) :
            valor = int(input(f"[{i + 1}][{j + 1}] : "))
            matriz[i][j] = valor
        print()
    
    mayor = 0
    for i in range(orden) :
        for j in range(orden) :
            if matriz[i][j] > mayor :
                mayor = int(matriz[i][j])

    print(f"\n*** Mayor elemento de la matriz : {mayor} ***")

    print("\n\nDesea ingresar mas datos? (Si/No)")
    respuesta = input("$ ")
    respuesta.lower()

    if respuesta == "no" :
        break

print("\n\n%%%%%% Gracias por usar el programa %%%%%")
