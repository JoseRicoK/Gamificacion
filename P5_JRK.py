num = int(input(f"\nIntroduce un número entre 1 y 10: "))
fichero = open("P5_tabla.txt", "w")
for i in range(1, 10+1):
    fichero.write(f"{str(num)} x {str(i)} = {str(num * i)}\n")
fichero.close()