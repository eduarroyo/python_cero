# 1. Usa un bucle while para imprimir los números del 1 al 10.
counter = 1
while counter <= 10:
    print(counter)
    counter += 1

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada número.
list = [10, 20, 30, 40, 50]
for n in list:
    print(n)

# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1

print(sum)

# 4. Escribe un bucle for que imprima cada carácter de la cadena "Python".
for c in "Python":
    print(c)

# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.
i = 1
while i <= 50:
    if i % 7 == 0:
        print(i)
        break
    i += 1


# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
dictionary = {"name": "Brais", "age": 37, "country": "Galicia"}
for key in dictionary.keys():
    print(key)

# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.
for i in range(1, 21, 1):
    if i % 2 == 0:
        print(i)

# 8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso.

for i in range(10,0,-1):
    print(i)

# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista[30, 10, 30, 20, 30, 40].
list = [30, 10, 30, 20, 30, 40]
count = 0
for n in list:
    if n == 30:
        count += 1

print(count)

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
nombres = ["Pepe", "Manuel", "Rafael", "Brais", "Miguel"]
for nombre in nombres:
    print(f"Nombre actual {nombre}.")
    if nombre == "Brais":
        break