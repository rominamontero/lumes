import time

espacios=90
registrados=0
historial=0

while True:
    print(''' MENU PRINTCIPAL
            1.- Espacios disponibles
            2.- Poner libros
            3.- Sacar libros
            4.- Historial de ocupaciones
            5.- Salir''')
    try:
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                print("ESPACIOS DISPONIBLES")
                print(f"Quedan {espacios} espacios disponibles")
            case 2:
                print("PONER LIBRO")
                if espacios>0:
                    print("Ha ingresado un libro")
                    registrados=registrados+1
                    historial=historial+1
                    espacios=espacios-1
                else:
                    print(f"No puede ingresar mas libros. No tiene espacio disponible")
            case 3:
                print("SACAR LIBROS")
                if historial<=0:
                    print("No hay libros para sacar")
                else:
                    print("Ha sacado un libro")
                    historial=historial-1
                    espacios=espacios+1
            case 4:
                print("HISTORIAL DE OCUPACIONES")
                print(f"Ha registrado {registrados} libros")
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
                op=int(input("Seleccione una opcion valida: "))
    except ValueError:
        print("Debe ingresar una opcion numerica")