class Person:
    """класс Person"""

    biological_species = "Homo sapiens"
    planet = "Earth"

    def say_hello():
        print("Hello World")


Person.say_hello()
print(Person.__dict__)

# {
#   '__module__': '__main__',
#   '__doc__': 'класс Person',
#   'biological_species': 'Homo sapiens',
#   'planet': 'Earth',
#   'say_hello': <function Person.say_hello at 0x7f460441d8a0>,
#   '__dict__': <attribute '__dict__' of 'Person' objects>,
#   '__weakref__': <attribute '__weakref__' of 'Person' objects>
# }

# Обращаем внимание на атрибут say_hello и его тип:
print(Person.__dict__["say_hello"])
#   <function Person.say_hello at 0x7f460441d8a0>


# Другие способы обращениея к callable-атрибуту класса
getattr(Person, "say_hello")()
Person.__dict__["say_hello"]()
