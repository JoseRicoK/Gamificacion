import os

file = "archivo7.txt" 
while True:
    print(f"Gestión de códigos")
    print(f"============================")
    print(f"1 - Consultar código de identificación")
    print(f"2 - Añadir código de un sistema nuevo")
    print(f"3 - Eliminar código")
    print(f"4 - Crear el gestor de códigos")
    print(f"0 - Terminar")
    option = input("\nIntroduce una opción: ")
    if option == "1":
        sist = input("Introduce el nombre del sistema: ")
        try: 
            f = open(file, "r")
        except FileNotFoundError:
            print(f"¡El fichero {file} no existe!\n")
        else:
            directory = f.readlines()
            f.close()
            directory = dict([tuple(line.split(",")) for line in directory])
            if sist in directory:
                print(f"---> {directory[sist]}")
            else:
                print(f"¡El código {sist} no existe!\n")
    elif option == "2":
        sist = input("Introduce el nombre del sistema: ")
        codigo = input("Introduce el código del sistema: ")
        try: 
            f = open(file, "a")
        except FileNotFoundError:
            print(f"¡El fichero {file} no existe!\n")
        else:
            f.write(sist + "," + codigo + "\n")
            f.close()
            print("El código se ha añadido.\n")
    elif option == "3":
        sist = input("Introduce el nombre del sistema: ")
        try: 
            f = open(file, "r")
        except FileNotFoundError:
            print(f"¡El fichero  {file} no existe!\n")
        else:
            directory = f.readlines()
            f.close()
            directory = dict([tuple(line.split(",")) for line in directory])
            if sist in directory:
                del directory[sist]
                f = open(file, "w")
                for name, codigo in directory.items():
                    f.write(name + "," + codigo)
                f.close()
                print(f"¡El cliente se ha borrado!\n")
            else:
                print(f"¡El cliente {sist} no existe!\n")        
    elif option == "4":
        if os.path.isfile(file):
            answer = input(f"El fichero {file} ya existe. ¿Desea vaciarlo (S/N)?: ")
            if answer == "N": 
                print(f"No se ha creado el fichero porque ya existe.\n")
        f = open(file, "w")
        f.close()
        print("Se ha creado el fichero\n")
    else:
        break