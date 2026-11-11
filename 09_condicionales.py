# # 1. Escribe un programa que verifique si un número es positivo, negativo o cero.
# try:
#     numero = int(input("Introduce un número: "))
#     if numero > 0:
#         print("positivo")
#     elif numero < 0:
#         print("negativo")
#     else:
#         print("cero")
# except ValueError:
#     print("¡Eso no era un número!")

# # 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o más) o menor de edad.
# try:
#     edad = int(input("Introduce tu edad: "))
#     if edad >= 18:
#         print("Eres mayor de edad")
#     else:
#         print("Eres menor de edad")
# except ValueError:
#     print("¡Eso no era un número!")

# # 3. Escribe un programa que verifique si una cadena de texto está vací­a y muestre un mensaje en consecuencia.
# cadena = input("Introduce un texto: ")
# if not cadena:
#     print("El texto está vacío")
# else:
#     print(cadena)

# # 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
# try:
#     numero1 = int(input("Introduce el primer número: "))
#     numero2 = int(input("Introduce el segundo número: "))
#     if numero1 > numero2:
#         print("El primero ese mayor")
#     elif numero2 > numero1:
#         print("El segundo es mayor")
#     else:
#         print("Son iguales")
# except ValueError:
#     print("¡Eso no era un número!")

# # 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.
# try:
#     numero = int(input("Introduce un número: "))

#     if numero % 3 == 0 and numero % 5 == 0:
#         print("El número es divisible por 3 y por 5")
#     else:
#         print("Ese número es aburrido")

# except ValueError:
#     print("¡Eso no era un número!")


# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.
# try:
#     numero = int(input("Introduce un número: "))

#     if numero % 2 == 0:
#         print("El número es par")
#     else:
#         print("El número es impar")

# except ValueError:
#     print("¡Eso no era un número!")


# # 7. Escribe un programa que determine si una persona puede votar en función de su edad(mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.
# try:
#     edad = int(input("Introduce tu edad: "))

#     if edad >= 18:
#         print("Puedes votar")
#     elif edad >= 16:
#         print("Puedes votar con un permiso especial")
#     else:
#         print(f"Debes esperar a tener {16-edad} años más para poder votar.")

# except ValueError:
#     print("¡Eso no era un número!")

# # 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.
# password_predefinida = "12345"
# password = input("Introduce la contraseña: ")
# if password == password_predefinida:
#     print("Error: Utiliza una contraseña segura")

# # 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).
# try:
#     numero = int(input("Introduce un número: "))

#     if numero >= 10 and numero <= 20:
#         print("El número está entre 10 y 20")
#     else:
#         print("El número no está entre 10 y 20")

# except ValueError:
#     print("¡Eso no era un número!")


# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.

color = input("Introduce el color del semáforo: ")
if color == "rojo":
    print("Detente")
elif color == "amarillo":
    print("Precaución")
elif color == "verde":
    print("Avanza")
else:
    print("Tú no sabes lo que es un semáforo")