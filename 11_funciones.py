# 1. Crea una función llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningún nombre, debe saludar diciendo "Hola, desconocido".
def personalized_greeting(nombre = "desconocido"):
    print(f"Hola {nombre}")

personalized_greeting("Edu")
personalized_greeting()

# 2. Escribe una función llamada "multiply" que reciba dos números como argumentos y retorne el resultado de multiplicarlos.
def multiply(first_number: int, second_number: int):
    return first_number * second_number

print(multiply(3,6))

# 3. Crea una función llamada "is_even" que reciba un número entero como argumento y retorne True si es par y False si es impar.
def is_even(number: int):
    return number % 2 == 0

print(is_even(1))
print(is_even(2))

# 4. Escribe una función llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayúsculas.
def convert_to_uppercase(text: str):
    return text.upper()

print(convert_to_uppercase("hola"))
#print(convert_to_uppercase(1)) #AttributeError: 'int' object has no attribute 'upper'

# 5. Crea una función llamada "arbitrary_sum" que reciba un número arbitrario de números como argumentos y retorne la suma de todos ellos.
def arbitrary_sum(*numbers: float):
    return sum(numbers)

print(arbitrary_sum(1,2,3,4,5))

# 6. Escribe una función llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.
def generate_full_greeting(nombre: str, apellido: str):
    return f"Hola {nombre} {apellido}"

print(generate_full_greeting("Eduardo", "Arroyo"))
print(generate_full_greeting(apellido="Arroyo", nombre="Eduardo"))

# 7. Crea una función llamada "power" que reciba dos números: base y exponente, y retorne el resultado de elevar la base al exponente.
def power(base: float, exponente: float):
    return base**exponente

print(power(5,3))

# 8. Escribe una función llamada "calculate_average" que reciba tres números y retorne su promedio.
def calculate_average(number1: float, number2: float, number3: float):
    return((number1 + number2 + number3)/3)

print(calculate_average(4,6,10))

# 9. Crea una función llamada "count_characters" que reciba una cadena de texto y retorne el número de caracteres que contiene.
def count_characters(text: str):
    return len(text)

print(count_characters("hola mundo!"))

# 10. Escribe una función llamada "display_messages" que reciba un número indefinido de cadenas y las imprima en mayúsculas, una por una, tal como se hizo en el archivo proporcionado.
def display_messages(*texts: str):
    for text in texts:
        print(text.upper())

display_messages("hola", "mundo", "en", "python")