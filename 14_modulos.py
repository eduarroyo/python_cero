# 1. Crea un módulo llamado "calculator" que contenga funciones para sumar, restar, multiplicar y dividir dos números. Importa este módulo en otro archivo y usa sus funciones.
import modules.calculator as calculator
print(calculator.sum(1,3))
print(calculator.difference(1,3))
print(calculator.multiply(1,3))
print(calculator.divide(1,3))

# 2. Crea un módulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. Escribe un programa que importe este módulo y realice conversiones.
from modules.converter import to_celsius, to_farenheit
print(to_celsius(234))
print(to_farenheit(0))

# 3. Crea un módulo que contenga una lista de nombres de estudiantes y una función que imprima todos los nombres. Importa este módulo en otro archivo y usa la función para mostrar la lista.
from modules.students import print_students
print_students()

# 4. Crea un módulo llamado "geometry" que tenga una función para calcular el área de un cí­rculo y un cuadrado. Usa este módulo en otro archivo para calcular áreas.
import modules.geometry as geometry
print(geometry.area_of_circle(6))
print(geometry.area_of_square(5))

# 5. Escribe un módulo que contenga una función que acepte cualquier número de argumentos y devuelva su suma. Importa y usa la función en otro archivo.
from modules.sums import sum_all
print(sum_all(1,2,3,4,5,6))

# 6. Crea un módulo que defina una clase llamada "Car" con propiedades como marca, modelo y año. Importa este módulo en otro archivo y crea una instancia de la clase "Car".
from modules.vehicles import Car
my_car = Car("Renault", "Megane", 2016)
print(my_car.vendor, my_car.model, my_car.year)

# 7. Escribe un módulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones para escribir y leer datos.
import modules.text_files as text_files
text_files.write_file("prueba.txt", "Esto es texto de prueba")
print(text_files.read_file("prueba.txt"))

# 8. Crea un módulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de números. Usa este módulo para calcular estos valores en una lista dada.
import modules.statistics as statistics
print(statistics.average(1,5,3,4))
print(statistics.median(1,5,4,4))

# 9. Crea un módulo que contenga una función para contar cuántas veces aparece una palabra en un texto. Escribe un programa que importe el módulo y lo use para contar palabras en una cadena.
from modules.texts import count_words
print(count_words("Crea un módulo que contenga una función para contar cuántas veces aparece una palabra en un texto. Escribe un programa que importe el módulo y lo use para contar palabras en una cadena."))

# 10 Crea un módulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas. Usa este módulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas especí­ficas.
from modules.dates import current_date, date_diff
print(current_date())
print(date_diff("2026-11-11T00:00:00", "2026-01-01T00:00:00"))