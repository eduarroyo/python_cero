# 1. Realiza las siguientes operaciones aritmÃ©ticas:
# â€¢	Suma: 15 + 25
# â€¢	Resta: 50 - 22
# â€¢	MultiplicaciÃ³n: 8 * 7
# â€¢	DivisiÃ³n: 100 / 20

# 2. Calcula el resto de la división de 37 entre 5 y almacÃ©nalo en una variable remainder. Luego imprÃ­melo.
remainder = 37 % 5
print(remainder)

# 3. Convierte el nÃºmero 7 en una cadena de texto y concatÃ©nalo con la frase â€œ es mi nÃºmero favoritoâ€. Imprime el resultado.
favorite_number = str(7) + " es mi número favorito"
print(favorite_number)

# 4. Repite la palabra "Python" 10 veces usando el operador de multiplicación para cadenas y luego imprímela.
python_repeated = "Python " * 10
print(python_repeated)

# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.
a = 12
b = 8
a_mayor_que_b = a > b
print(a_mayor_que_b)

# 6. Compara dos cadenas de texto ("apple" y "banana") usando los operadores > y < y explica cuál tiene mayor orden alfabético.
if "apple" > "banana":
    print('"apple" tiene mayor orden alfabético que "banana".')
else:
    print('"banana" tiene mayor orden alfabético que "apple".')

# 7. Realiza una comparaciÃ³n lÃ³gica usando and para verificar si el nÃºmero 10 es mayor que 5 y menor que 20. Imprime el resultado.
expresion_logica = 10 > 5 and 10 < 20
print(expresion_logica)

# 8. Usa el operador or para verificar si el nÃºmero 7 es menor que 3 o mayor que 5. Imprime el resultado.
expresion_logica = 7 < 3 or 7 > 5
print(expresion_logica)

# 9. Aplica el operador not para invertir el resultado de la comparaciÃ³n 15 > 20. Â¿CuÃ¡l es el resultado?
expresion_logica = not (15 > 20)
print(expresion_logica)

# 10. Combina operadores aritméticos y lógicos: Verifica si el número resultante de la expresión (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.
resultado = (5 * 3) + 2
expresion_logica = resultado > 10 and resultado < 20    
print(expresion_logica)