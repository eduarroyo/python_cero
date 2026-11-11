# # 1. Crea una función que intente dividir dos números proporcionados por el usuario. Usa try-except para capturar cualquier error de división (por ejemplo, división por cero).
# try:
#     dividendo = float(input("Introduce el dividendo: "))
#     divisor = float(input("Introduce el divisor:"))
#     print(f"Resultado: {dividendo / divisor}")
# except ValueError as ve:
#     print("Eso no era un número real", ve)
# except ZeroDivisionError as zde:
#     print("División por cero", zde)
# except Exception as ex:
#     print("Otro error", ex)

# # 2. Crea una función que tome una cadena e intente convertirla en un número entero. Usa try-except para capturar cualquier error en la conversión.
# def pide_numero():
#     cadena = input("Introduce un número entero: ")
#     return int(cadena)

# try:
#     print(pide_numero())
# except ValueError as ve:
#     print("Eso no era un número entero", ve)

# # 3. Crea una función que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura.
# def read_file(filename):
#     with open(filename, 'r') as file:
#         content = file.read()
#         print(content)

# ruta = "texto_ejemplo.txt"
# ruta_falsa = "fichero_falso.txt"
# try:
#     read_file(ruta)
#     read_file(ruta_falsa)
# except FileNotFoundError as fnfe:
#     print(fnfe)

# # 4. Crea una función que realice múltiples operaciones (suma, resta, división, multiplicación) con dos números. Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de los errores.
# def operations(number1: float, number2: float):
#     try:
#         print(f"Suma: {number1+number2}")
#         print(f"Resta: {number1-number2}")
#         print(f"Multiplicación: {number1*number2}")
#         print(f"División: {number1/number2}")
#     except ZeroDivisionError as zde:
#         print("No se puede dividir por cero:", zde)
#     else:
#         print("Operaciones realizadas")
#     finally:
#         print("Fin de operations")

# operations(5,2)
# operations(4,0)

# # 5. Crea una función que le pida al usuario su edad y lance un ValueError si la entrada no es un número entero positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario.
# def pide_edad():
#     edad = int(input("Introduce la edad: "))
#     if edad <= 0:
#         raise ValueError("La edad debe ser un entero positivo")
        
# try:
#     pide_edad()
# except ValueError as ve:
#     print("Error:", ve)
# finally:
#     print("Fin de pide_edad")


# # 6. Crea una función que intente acceder a un elemento de una lista por í­ndice. Usa try-except para manejar el caso donde el índice esté fuera de rango.
# def get_element_by_index(list: list, index: int):
#     try:
#         return list[index]
#     except IndexError as ie:
#         print("Índice fuera de rango:", ie)

# print(get_element_by_index([1,2,3], 2))
# print(get_element_by_index([1,2,3], 6))

# # 7. Crea una función que use try-except para manejar múltiples excepciones: ZeroDivisionError, ValueError y TypeError.
# def multiple_exceptions(number1: float, number2: float):
#     try:
#         result = number1 / number2
#         print(f"Resultado: {result}")
#     except ZeroDivisionError as zde:
#         print(zde)
#     except ValueError as ve:
#         print(ve)
#     except TypeError as te:
#         print(te)

# multiple_exceptions(1,2)
# multiple_exceptions(1,0)
# multiple_exceptions("asdf", 5)
# multiple_exceptions(5, { "hola" })

# # 8. Crea una función que simule una transacción. Lanza una excepción personalizada llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar.
# class InsufficientFundsError(Exception):
#     pass

# def simulate_transaction(balance: float, withdrawal_ammount: float):
#     if withdrawal_ammount > balance:
#         raise InsufficientFundsError("Saldo insuficiente")
#     balance -= withdrawal_ammount
#     print(f"Transacción realizada. Saldo {balance}")

# try:
#     simulate_transaction(1234, 44)
#     simulate_transaction(1234, 1236)    
# except InsufficientFundsError as ife:
#     print("Error:", ife)

# # 9. Crea una función que intente convertir una lista de cadenas en enteros. Maneja cualquier error que surja cuando una cadena no pueda convertirse.
# def to_int_list(*str_numbers: str):
#     my_list = []
#     for string in str_numbers:
#         try:
#             my_list.append(int(string))
#         except ValueError as ve:
#             print(f"Error al procesar {string}:", ve)
#         except TypeError as te:
#            print(f"Error al procesar {string}", te)
#     return my_list

# print(to_int_list("1","2","3","4"))
# print(to_int_list("1",{ "valor": 4},"3","asdf"))

# # 10. Crea una función que calcule la raí­z cuadrada de un número. Lanza un ValueError si el número es negativo.
# def secure_sqrt(number: float):
#     if number < 0:
#         raise ValueError("No se pueden calcular raíces cuadradas de números negativos.")

#     return number**1/2

# try:
#     print(secure_sqrt(2))
#     print(secure_sqrt(16))
#     print(secure_sqrt(-5))
# except ValueError as ve:
#     print(ve)