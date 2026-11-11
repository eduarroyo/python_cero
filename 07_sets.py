# 1. Crea un set con los números del 1 al 5 e imprí­melo.
pruebas_set = {1,2,3,4,5}
print(type(pruebas_set))
print(pruebas_set)

# 2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprí­melo.
pruebas_set.add(6)
print(pruebas_set)

# 3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Qué sucede?
pruebas_set.add(5)
print(pruebas_set) # No se añade porque el valor 5 ya estaba en el set. Parece que los set en python mantienen colecciones de elementos únicos.

# 4. Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e imprime el resultado.
contains3 = 3 in pruebas_set
contains7 = 7 in pruebas_set
print(contains3, contains7)

# 5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
pruebas_set.remove(4)
print(pruebas_set)

# 6. Usa el método clear() para vaciar un set y luego imprime su longitud.
pruebas_set.clear()
print(pruebas_set)

# 7. Convierte el set {"manzana", "naranja", "plátano"} en una lista e imprime el primer elemento de la lista.
frutas_set = {"manzana", "naranja", "plátano"}
my_list = list(frutas_set)
print(my_list[0])

# 8. Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set_union = set1.union(set2)
print(set_union)

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
set_difference = {1, 2, 3, 4} - {3, 4, 5, 6}
print(set_difference)

# 10. Elimina un set llamado pruebas_set usando del y luego intenta imprimirlo para ver el resultado.
my_set = { "a", "b", "c" }
del my_set
# print(my_set) #NameError: name 'my_set' is not defined

