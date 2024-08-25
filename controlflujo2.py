estudiantes = [
 {"nombre": "Juan", "edad": 17, "calificaciones": [85, 90, 88]},
 {"nombre": "María", "edad": 19, "calificaciones": [92, 89, 90]},
 {"nombre": "Pedro", "edad": 21, "calificaciones": [85, 95, 80]},
 {"nombre": "Ana", "edad": 18, "calificaciones": [90, 92, 87]},
 {"nombre": "Luis", "edad": 20, "calificaciones": [88, 85, 92]},
]

#Dado que el ejercicio se expresa de manera ambigua, se crean dos resultados distintos.
"""
#Primer resutado considerando los el filtro y el calculo por separado:
print("Estudiantes de edad mayor a 18 años y con un promedio de calificaciones mayor a 85 son: ")
for estudiante in estudiantes:
    if (estudiante["edad"]>18 and (sum(estudiante["calificaciones"])/ len(estudiante["calificaciones"]))>85):
        print(estudiante)
print (estudiante)

print()
print ("Promedio de calificación para estudiantes mayor a 18 años y que su edad sea un numero primo es: ")
for estudiante in estudiantes:
    if estudiante["edad"]>18:
        for i in range (2,estudiante["edad"]):
            if estudiante["edad"] % i == 0:
                break
        else:
            promedio = sum(estudiante["calificaciones"])/ len(estudiante["calificaciones"])
            print("Promedio: ", promedio, estudiante)
"""

print ()
#Segundo resultado considerando ambos filtro y calculo de promedio en conjunto:
print("Los estudiantes mayor de 18 años de edad, con promedio mayor a 85 y con una edad en numero primo es:")
for estudiante in estudiantes:
    promedio = sum(estudiante["calificaciones"])/ len(estudiante["calificaciones"])
    if (estudiante["edad"] > 18 and promedio > 85):
        for i in range (2,estudiante["edad"]):
            if estudiante["edad"] % i == 0:
                break
        else:
            print(estudiante, "promedio: ", promedio)