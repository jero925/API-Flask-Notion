import math

print(math.sqrt(25))

print("hola mundo")

letra = "pepe"
edad = 20

def saludar(nombre):
    print("saludos, " + nombre + "!")

saludar("Pepe")

if edad > 18:
    print("mayor de edad")
else:
    print("Menor")

## for, while
    
for i in range(5):
    print(i)

while edad < 30:
    print("muy pibardo")
    edad += 1

#Input 
nombre = input("Ingresa nombre papurrix: ")
saludar(nombre)