indie=0
estudio=0
cont=0
contA=0
contM=0

while True:

    nombre=input("Ingrese el nombre del juego: ")

    while True:
        if len(nombre) >= 5 and " " not in nombre: 
            break
        else:
            print("Error el nombre no debe tener espacios y debe tener 5 caracteres como minimo")
            nombre=input("Ingrese el nombre del juego: ")

    while True:
        try:
            precio=int(input("Ingrese el precio: "))
            if precio <=0 :
                print("Error, el precio debe ser mayor que cero")
            else:
                break
        except ValueError:
            print("Debe ingresar solo numeros")

    if precio >= 20000 and precio >= 40000:
        indie+=1
    elif precio< 40000:
        estudio+=1

    while True:
        clasificacion=input("Ingrese la clasificacion (E (<12), A (+12) o M (+18)): ")
        if clasificacion=="E": 
            cont+=1
            break
        elif clasificacion=="A":
            contA+=1
            break
        elif clasificacion =="M":
            contM+=1
            break
    print(f"Hay {indie} indies, {estudio} de estudio. Solo {cont} son de clasificacion E")
    continuar=input("Desea continuar S/N:  ")
    if continuar=="N":
        break

