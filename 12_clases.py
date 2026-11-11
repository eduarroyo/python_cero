# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un método "make_sound" que imprima un sonido genérico.
# class Animal:
#     def __init__ (self):
#         self.species = "orangután"

#     def make_sound(self):
#         print("gulifrisqui!")

# my_animal = Animal()
# print(my_animal.species)
# my_animal.make_sound()

# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacénala en una propiedad pública. Añade el método "make_sound" que imprima un sonido dependiendo de la especie.
class Animal:
    def __init__ (self, species: str):
        self.species = species

    def make_sound(self):
        if self.species == "Lion":
            print("Roarrr!")
        else:
            print("gulifrisqui!")

my_animal1 = Animal("Lion")
print(my_animal1.species)
my_animal1.make_sound()
my_animal2 = Animal("Monkey")
print(my_animal2.species)
my_animal2.make_sound()

# 3. Crea una clase llamada "Car" con las propiedades públicas "brand" y "model". Además, debe tener una propiedad privada "_speed" que inicialmente será 0.
# class Car:
#     _speed: str

#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         _speed = 0

# my_car = Car("Renault", "Megane")
# print(my_car.brand, my_car.model)

# 4. Añade a la clase "Car" un método llamado "accelerate" que aumente la velocidad en 10 unidades. Añade también un método "brake" que reduzca la velocidad en 10 unidades. Asegúrate de que la velocidad no sea negativa.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__speed = 0

    def accelerate(self):
        self.__speed += 10

    def brake(self):
        self.__speed -= 10
        if(self.__speed < 0):
            self.__speed = 0

    def print_speed(self):
        print(self.__speed)

my_car = Car("Renault", "Megane")
print(my_car.brand, my_car.model)
my_car.print_speed()
my_car.accelerate()
my_car.print_speed()
my_car.accelerate()
my_car.accelerate()
my_car.print_speed()
my_car.brake()
my_car.print_speed()
my_car.brake()
my_car.brake()
my_car.print_speed()

# 5. Crea una clase "Book" que tenga propiedades como "title" (público) y "author" (privado). Añade un método para obtener el autor y otro para cambiar el tí­tulo del libro.
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.__author = author

    def get_author(self):
        return self.__author

    def set_title(self, new_title):
        self.title = new_title

my_book = Book("La Fundació", "Isaac Asimov")
print(f"{my_book.title} {my_book.get_author()}")
my_book.set_title("La fundación")
print(f"{my_book.title} {my_book.get_author()}")

# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. Añade un método para calcular y devolver la nota media del estudiante.
class Estudiante:
    def __init__(self, nombre:str, apellido: str, notas:list):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__notas = notas

    def media(self):
        return sum(self.__notas)/len(self.__notas)

my_student = Estudiante("Pepe", "Pérez", [5,7,10])
print(my_student.media())

# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". Añade métodos para depositar y retirar dinero, asegurándote de que no se pueda retirar más de lo que hay en la cuenta.
class BankAccount:
    def __init__(self, owner, balance:float):
        self.__owner = owner
        self.__balance = balance

    def ingresar(self, monto:float):
        self.__balance += monto

    def retirar(self, monto: float):
        if(self.__balance < monto):
            return
        self.__balance -= monto

    def balance(self):
        return self.__balance

my_account = BankAccount("edu", 100.0)
print(my_account.balance())
my_account.retirar(101.0)
print(my_account.balance())
my_account.retirar(50.0)
print(my_account.balance())
my_account.ingresar(200)
print(my_account.balance())

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". Añade un método que calcule la distancia entre dos puntos.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceTo(self, point: Point):
        return ((self.x-point.x)**2+(self.y-point.y)**2)**(1/2)

point1 = Point(1, 1)
point2 = Point(0,0)
print(point1.distanceTo(point2))

# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". Añade un método que calcule el pago total basado en las horas trabajadas y el salario por hora.
class Employee:
    def __init__(self, name:str, hourly_wage:float):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = 0

    def total_wage(self):
        return self.hourly_wage*self.hours_worked

my_employee = Employee("Edu", 100)
my_employee.hours_worked = 40
print(my_employee.total_wage())

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). Añade un método para agregar un producto al inventario y otro para mostrar todos los productos disponibles.
class Store:
    def __init__(self):
        self.__inventory = []

    def add_to_inventory(self, product: str):
        self.__inventory.append(product)

    def print_inventory(self):
        print(self.__inventory)

my_store = Store()
my_store.add_to_inventory("folio")
my_store.add_to_inventory("lápiz")
my_store.add_to_inventory("bolígrafo")
my_store.print_inventory()