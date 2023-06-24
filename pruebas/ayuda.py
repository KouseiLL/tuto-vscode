# Definimos las listas para almacenar los datos
materias = ["Matemáticas", "Física", "Química", "Inglés"]
calificaciones_p1 = []
calificaciones_p2 = []
promedios = []

# Obtenemos los datos del estudiante
numero_control = input("Ingrese el número de control del estudiante: ")
nombre = input("Ingrese el nombre del estudiante: ")
carrera = input("Ingrese la carrera del estudiante: ")
semestre = int(input("Ingrese el semestre del estudiante: "))

# Obtenemos las calificaciones de cada materia
for materia in materias:
    calificacion_p1 = float(input("Ingrese la calificación del primer parcial de " + materia + ": "))
    calificacion_p2 = float(input("Ingrese la calificación del segundo parcial de " + materia + ": "))
    calificaciones_p1.append(calificacion_p1)
    calificaciones_p2.append(calificacion_p2)
    promedio = (calificacion_p1 + calificacion_p2) / 2
    promedios.append(promedio)

# Imprimimos la boleta del estudiante
print("Boleta de calificaciones")
print("Número de control:", numero_control)
print("Nombre:", nombre)
print("Carrera:", carrera)
print("Semestre:", semestre)

for i in range(len(materias)):
    print("--------------------------------------")
    print(materias[i])
    print("Calificación primer parcial:", calificaciones_p1[i])
    print("Calificación segundo parcial:", calificaciones_p2[i])
    print("Promedio:", promedios[i])

    if promedios[i] < 7:
        print("El estudiante debe repetir el curso.")
