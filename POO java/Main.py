from poo import *

#creamos 3 personas llamando el metodo "init" de persona de la clase para asi crear cada una
#con los atributos qe pide dicho metodo

estudiante1 = Persona("camilo",19,1.70,73,"H")
estudiante2 = Persona("juan",18,1.68,75,"H")
estudiante3 = Persona("maria",13,1.60,54,"M")

estudiante4 = Estudiante("luisa",20,1.60,60,"M","Odontologia",6)
estudiante5 = Estudiante("Carlos",20,1.75,80,"H","Sistemas",2)

empleado = Empleado("a",1,1,1,1,"H",1)
empleado1 = Empleado("nicolas",19,1.80,80,"H","profesor",150000000)
empleado2 = Empleado("fernanda",20,1.75,72,"M","profesora",1300000)

print("estudiante 1: ")
print(estudiante1)
print("estudiante 2: ")
print(estudiante2)
print("estudiante 3: ")
print(estudiante3)
print("--------------------------------------------------------------------------------")
print("estudiante 4: ")
print(estudiante4)
print("estudiante 5: ")
print(estudiante5)
print("empleado 1: ")
print(empleado1)
print("empleado 2: ")
print(empleado2)