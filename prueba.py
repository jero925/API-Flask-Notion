# import math

# print(math.sqrt(25))

# print("hola mundo")

# LETRA = "pepe"
# EDAD = 20

# def saludar(nombrePersona):
#     print("saludos, " + nombrePersona + "!")

# saludar("Pepe")

# if EDAD > 18:
#     print("mayor de EDAD")
# else:
#     print("Menor")

# ## for, while
    
# for i in range(5):
#     print(i)

# while EDAD < 30:
#     print("muy pibardo")
#     EDAD += 1

# nombre = input("Ingresa nombre papurrix: ")
# saludar(nombre)

def imprimir_numeros_pares_hasta_n(n):
    """"
    Imprime todos los numeros pares desde 0 hasta el numero n (incluido)
    """
    for i in range (n + 1):
        if i % 2 == 0:
            print(i)
        else:
            print(f"{i} (Impar)")

#Usar la funcion
LIMITE = 10
imprimir_numeros_pares_hasta_n(LIMITE)