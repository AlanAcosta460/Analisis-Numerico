print("%%%%% Bienvenido al programa %%%%%")
print("\n*** Factorial de un numero entero ***")

while True :
    print("\nPor favor ingrese un numero entero positivo")
    n = int(input("$ "))

    if n < 0 :
        print("\n\t\t*** El numero debe ser positivo ***\n")
        continue
    
    resultado = 1
    for num in range(1, n + 1) :
        resultado *= num

    print(f"\n*** El factorial de {n} es : {resultado}")

    print("\n\nDesea ingresar otro numero? (Si/No)")
    respuesta = input("$ ")
    respuesta.lower()

    if respuesta == "no" :
        break

print("\n\n%%%%%% Gracias por usar el programa %%%%%")
