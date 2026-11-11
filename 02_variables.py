my_var = 1
print(type(my_var), my_var)
my_var = "hola"
print(type(my_var), my_var)

# 1. Declara y asigna valores a las siguientes variables:
#   · name: una cadena que contenga tu nombre.
#   · age: un número entero que represente tu edad.
#   · height: un número flotante que represente tu altura.
#   · Imprime cada variable en una línea separada.

name = "Eduardo"
age = 42
height = 1.75

print(name)
print(age)
print(height)

# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuántos años tienes.
print("Tengo " + str(age) + " años.")

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False según corresponda e imprímela.
is_student = True
print(is_student)

# 4. Usa la función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.
full_name = "Eduardo Arroyo Ramírez"
print(len(full_name))

# 5. Declara tres variables en una sola línea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
name, surname, city = "Eduardo", "Arroyo", "Écija"
print(name, surname, city)

# 6. Usa la funciÃ³n input() para solicitar al usuario su color favorito y almacÃ©nalo en una variable color. Luego, imprime el valor ingresado.
color = input("¿Cuál es tu color favorito? ")
print("Tu color favorito es: " + color)

# 7. Declara una variable fruit e inicialí­zala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit = "manzana"
print(fruit)
fruit = "banana"
print(fruit)

# 8. Convierte un nÃºmero decimal, almacenado en la variable price, a un nÃºmero entero y luego imprÃ­melo.
price = 19.99
print(int(price))

# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una direcciÃ³n usando la funciÃ³n len(). Imprime el resultado.
address = "Calle Principal, 123"
address_len = len(address)
print(address_len)

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre será un número. Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().
phone = int(1234567890)
phone = 999999999
print(type(phone))