class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person = Person("Reverend", 30)
# Menambah atribut address secara dinamis
person.address = "California"
# Mengubah nilai atribut age secara dinamis
person.age = 35
print(person.name)
print(person.age)
print(person.address)