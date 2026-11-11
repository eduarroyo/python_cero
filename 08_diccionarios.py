# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.
my_dictionary = {
    "name": "Eduardo",
    "age": 42,
    "country": "Spain"
}
print(my_dictionary)

# 2. Accede al valor de la clave name en el diccionario.
print(my_dictionary["name"])

# 3. AÃ±ade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
my_dictionary["job"] = "Programador"
print(my_dictionary)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
my_dictionary["age"] = 38
print(my_dictionary)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
del my_dictionary["country"]
print(my_dictionary)

# 6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
squares = {
    1: 1**2,
    2: 2**2,
    3: 3**2,
    4: 4**2,
    5: 5**2,
}
print(squares)

# 7. Verifica si la clave age está presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.
brais_dict = {"name": "Brais", "age": 37, "country": "Galicia"}
(print("age" in brais_dict))

# 8. Imprime solo las claves del diccionario.
print(brais_dict.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
keys = list(brais_dict.keys())
print(keys)

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".
keys = ["name", "age", "job"]
my_dict = dict.fromkeys(keys, "desconocido")
print(my_dict)