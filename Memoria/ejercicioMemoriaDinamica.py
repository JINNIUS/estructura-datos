# Hacer un programa que capture los siguientes datos de alumnos
# Nombre, ApellidoPaterno, ApellidoMaterno
# Fecha de Nacimiento en formato add/mm/aaaa
# guardar los datos de objetos 
# mostrar esos objetos

class Alumno:
    def __init__(self, nombre, ApellidoPaterno, ApellidoMaterno, fecha_nacimiento):
        self.nombre = nombre
        self.ApellidoPaterno = ApellidoPaterno
        self.ApellidoMaterno = ApellidoMaterno
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
            return f"Nombre: {self.nombre}\nApellido Paterno: {self.ApellidoPaterno}\nApellido Materno: {self.ApellidoMaterno}\nFecha de Nacimiento: {self.fecha_nacimiento}"
    
alumnos = []

while True:
     nombre = input("Ingrese el nombre del alumno: ")
     ApellidoPaterno = input("Ingrese el apellido paterno del alumno: ")
     ApellidoMaterno = input("Ingrese el apellido materno del alumno: ")
     fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno en formato dd/mm/aaaa: ")
     alumno = Alumno(nombre, ApellidoPaterno, ApellidoMaterno, fecha_nacimiento)
     alumnos.append(alumno)
     continuar = input("¿Deseas agregar otro alumno?(si/no): ")
     if continuar.lower() == "no":
          break
for alumno in alumnos:
     print(alumno)