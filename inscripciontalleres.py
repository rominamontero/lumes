import time

cupos=30

inscripcionesact=0
inscritos=0

tallere=0
tallera=0

basico=0
intermedio=0
avanzado=0


while True:
    print('''MENU PRINCIPAL
            1.- Cupos disponibles
            2.- Inscribir participantes
            3.- Retirar participantes
            4.- Estadisticas
            5.- Salir''')
    try:
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                print("CUPOS DISPONIBLES")
                print(f"Quedan {cupos} cupos disponibles ")
            case 2:
                print("INSCRIBIR PARTICIPANTES")
                if cupos>0:
                    while True:
                        codigo=input("Ingrese el codigo del taller: ")
                        if len(codigo)<5:
                            print("Error, el codigo debe tener minimo 5 caracteres, no debe tener espacios y debe estar en mayusculas")
                        elif " " in codigo:
                            print("Error, el codigo debe tener minimo 5 caracteres, no debe tener espacios y debe estar en mayusculas")
                        elif not codigo.isupper():
                            print("Error, el codigo debe tener minimo 5 caracteres, no debe tener espacios y debe estar en mayusculas")
                        else:
                            break
                    while True:
                        try:
                            precio=int(input("Ingrese el precio del taller: "))
                            if precio<=0:
                                print("Debe ingresar un valor mayor a 0")
                            else: 
                                break
                        except ValueError:
                            print("Debe ingresar un valor numerico")
                    if precio <= 30000:
                        tallere+=1
                    elif precio > 30000:
                        tallera+=1
                    while True:
                        clasificacion=input("Ingrese la categoria del taller B (basico), I (intermedio) o A (avanzado): ").upper()
                        if clasificacion=="B":
                            basico+=1
                            break
                        elif clasificacion=="I":
                            intermedio+=1
                            break
                        elif clasificacion=="A":
                            avanzado+=1
                            break
                        else:
                            print("Ingrese una opcion valida. B, I o A")
                    inscripcionesact=inscripcionesact+1
                    inscritos=inscritos+1
                    cupos=cupos-1
                    print("Participante inscrito correctamente")
                else:
                    print("No hay cupos disponibles")
            case 3:
                print("RETIRAR PARTICIPANTES")
                if inscripcionesact>0:
                    cupos=cupos+1
                    inscripcionesact=inscripcionesact-1
                    print("Participante retirado exitosamente")
                else:
                    print("No hay participantes inscritos")
            case 4:
                print("ESTADISTICAS")
                print(f"Total inscritos: {inscritos}")
                print(f"Inscritos actualmente: {inscripcionesact}")
                print(f"Cupos disponibles: {cupos}")
                print(f"Cantidad de talleres economicos: {tallere}")
                print(f"Cantidad de talleres avanzados: {tallera}")
                print(f"Cantidad categoria B: {basico}")
                print(f"Cantidad categoria I: {intermedio}")
                print(f"Cantidad categoria A: {avanzado}")
            case 5:
                print("SALIENDO")
                time.sleep(0.5)
                print(".")
                time.sleep(0.5)
                print(".")
                time.sleep(0.5)
                print(".")
                break
            case _:
                print("Opcion invalida")
    except ValueError:
        print("Debe ingresar una opcion numerica")