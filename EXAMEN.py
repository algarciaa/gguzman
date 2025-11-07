def gestor_notas_avanzado():
    print("GESTOR DE NOTAS AVANZADO")
    while True:
        try:
            num_estudiantes = int(input("Ingrese la cantidad de estudiantes a registrar: "))
            if num_estudiantes > 0:
                break
            else:
                print("ERROR: Ingrese un número entero positivo.")
        except ValueError:
            print("ERROR: Ingrese un número válido.")
    
    while True:
        try:
            numNotas = int(input("\nIngrese la cantidad de estudiantes a registrar: "))
            if numNotas> 0:
                break
            else:
                print("ERROR: Ingrese un número entero positivo.")
        except ValueError:
            print("ERROR: Ingrese un número válido.")
    
    nombres = []
    promedios = []
    
    print(f"REGISTRANDO {num_estudiantes} ESTUDIANTES ")

    for i in range(num_estudiantes):
        print(f"\n[Estudiante #{i + 1}]")
        while True:
            nombre = input("Ingrese el nombre del estudiante: ").strip()
            if nombre:
                break
            else:
                print("El nombre no puede estar vacío.")
        nombres.append(nombre)

    for i in range(numNotas):
        print(f"\n[Estudiante #{i + 1}]")
        while True:
            promedios = input("Ingrese la nota del Estudiante: ").strip()
            if promedios:
                break
            else:
                print("El nombre no puede estar vacío.")
        nombres.append(promedios)
    suma_notas= 0
    
    for j in range(numNotas):
            suma_notas += int(promedios[j])
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




    print("\nESTUDIANTES REGISTRADOS:")
    for i in range(num_estudiantes):
        print(f"\n[Estudiante #{i + 1}]")
        print(f"Nombre: {nombres[i]}")
        print(f"Promedio: {promedios[i]}")



if __name__ == "__main__":
    gestor_notas_avanzado()