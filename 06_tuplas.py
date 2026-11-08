# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.
tupla = (10, 20, 30, 40, 50)
print(tupla)

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.
tupla = (100, 200, 300, 400, 500)
print(tupla[1])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
tupla = (1, 2, 3)
# tupla[0] = 10  # Esto causará un error porque las tuplas son inmutables

# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
tupla = (1, 2, 3, 3, 4, 5, 3)
count_3 = tupla.count(3)
print(count_3)

# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
tupla = ("Java", "Python", "JavaScript", "Python")
index_python = tupla.index("Python")
print(index_python)

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
tupla_1 = (1, 2, 3)
tupla_2 = (4, 5, 6)
tupla_resultante = tupla_1 + tupla_2
print(tupla_resultante)

# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
tupla = (10, 20, 30, 40, 50)
subtupla = tupla[2:4]
print(subtupla)

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.
tupla = ("rojo", "verde", "azul")
lista = list(tupla)
lista[1] = "amarillo"
tupla = tuple(lista)
print(tupla)

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
my_tuple = (1, 2, 3)
del my_tuple
# print(my_tuple)  # Esto causará un error porque la tupla ha sido eliminada

# 10. Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
tupla = (100,)
print(tupla)