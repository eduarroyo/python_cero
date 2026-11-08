# 1. Declara una variable text con la frase "Aprendiendo Python" y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"
print(len(text))

# 2. Concatena dos cadenas: "Hola" y "Python", y muestra el resultado en una sola lí­nea.
print("Hola" + " " + "Python")

# 3. Crea una cadena que incluya un salto de lí­nea, y luego imprí­mela para ver el resultado.
print("Primera línea\nsegunda línea")

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
name="Eduardo"
surname="Arroyo"
age=42
print(f"Mi nombre es {name}, mi apellido es {surname} y tengo {age} años.")

# 5. Desempaqueta los caracteres de la palabra "Python" en variables separadas y luego imprí­melos uno por uno.
p, y , t, h, o, n = "Python"
print(p, y, t, h, o, n)

# 6. Extrae un "slice" de la palabra "Programación" para obtener los caracteres desde la posición 3 hasta la 7.
chunk = "Programación"[3:8]
print(chunk)

# 7. Invierte la cadena "Python" usando slicing y muestra el resultado.
reversed_text = "Python"[::-1]
print(reversed_text)

# 8. Convierte la cadena "aprendiendo python" en mayúsculas usando el método adecuado e imprí­mela.
text = "aprendiendo python"
print(text.upper())

# 9. Cuenta cuántas veces aparece la letra "n" en la cadena "Programación en Python".
count_n = "Programación en Python".count("n")
print(count_n)

# 10. Verifica si la cadena "12345" es numérica usando el método adecuado e imprime el resultado.
is_numeric = "12345".isnumeric()
print(is_numeric)
