def gestor_notas_avanzado():
    print("NOTAS ESTUDIANTES")
    print("")

    while True:
        try:
            num_estudiantes = int(input("Ingrese la cantidad de ESTUDIANTES a registrar: "))
            if num_estudiantes > 0:
                break
            else:
                print("ERROR: Ingrese un número entero positivo.")
        except ValueError:
            print("ERROR: Ingrese un número válido.")
    
    while True:
        try:
            numNotas = int(input("Ingrese la cantidad de NOTAS a registrar: "))
            if numNotas> 0:
                break
            else:
                print("ERROR: Ingrese un número entero positivo.")
        except ValueError:
            print("ERROR: Ingrese un número válido.")
    
    nombres = []
    promedios = []
    
    for i in range(num_estudiantes):
        print(f"[Estudiante #{i + 1}]")

        while True:
            nombre = input("Ingrese el nombre del estudiante: ").strip()
            if nombre:
                break
            else:
                print("El nombre no puede estar vacío.")
        nombres.append(nombre)

        suma_notas = 0
        for j in range(numNotas):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota #{j + 1} (0 a 10): "))
                    if 0 <= nota <= 10:
                        suma_notas += nota
                        break
                    else:
                        print("La nota debe estar entre 0 y 10.")
                except ValueError:
                    print("Ingrese un número válido.")

        promedio = suma_notas / numNotas
        promedios.append(promedio)


    aprobados = sum(1 for p in promedios if p >= 7)
    reprobados = sum(1 for p in promedios if p < 7)
    
    print("CALIFICACIONES")
    print("")
    
    
    


    print("ESTADO DE LOS ESTUDIANTES Y SUS NOTAS:")
    for i in range(num_estudiantes):
        print("")
        print(f"[Estudiante #{i + 1}]")
        print(f"Nombre: {nombres[i]}")
        print(f"Promedio: {promedios[i]}")
        if promedios[i] >= 7:
            print("Estado: APROBADO")
            print("")
        else:
            print("Estado: REPROBADO")
    print("")   
    print(f"ESTUDIANTES REPROBADOS: {aprobados}")
    print(f"ESTUDIANTES APROBADOS: {reprobados}")
    




if __name__ == "__main__":
    gestor_notas_avanzado()