indie=0
estudio=0
cont=0
contA=0
contM=0

while True:

    while True:
        nombre = input("Ingrese el nombre del juego: ")
        if len(nombre) < 5:
            print("Error: el nombre debe tener 5 caracteres como mínimo")
        elif " " in nombre:
            print("Error: el nombre no debe tener espacios")
        elif not nombre.isupper():
            print("Error: el nombre debe estar en MAYUSCULAS")
        else:
            break

    while True:
        try:
            precio=int(input("Ingrese el precio: "))
            if precio <=0 :
                print("Error, el precio debe ser mayor que cero")
            else:
                break
        except ValueError:
            print("Debe ingresar solo numeros")

    if precio <= 40000:
        indie+=1
    elif precio > 40000:
        estudio+=1

    while True:
        clasificacion=input("Ingrese la clasificacion (E (<12), A (+12) o M (+18)): ").upper()
        if clasificacion=="E": 
            cont+=1
            break
        elif clasificacion=="A":
            contA+=1
            break
        elif clasificacion =="M":
            contM+=1
            break
        else:
            print("Error: debe ingresar E, A o M")
    print(f"Hay {indie} indies, {estudio} de estudio. Solo {cont} son de clasificacion E, {contA} de clasificacion A y {contM} de clasificacion M")
    continuar=input("Desea continuar S/N:  ").upper()
    if continuar=="N":
        break

