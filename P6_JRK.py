num = int(input(f"\nIntroduce un número entre 1 y 10: "))
try: 
    archivo = open(f"P6_tabla{str(num)}.txt", "r")
except FileNotFoundError:
    print(f"\nNo disponemos de la tabla del {num}")
else:
    print(archivo.read())
    