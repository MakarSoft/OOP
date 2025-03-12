class Animal:
    eyes = 2
    legs = 4

    def eat(self, food):
        return f"Yum, yum, yum ({food})"

class Descriptor:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if isinstance(value, str):
            instance.__dict__[self.name] = value
        else:
            raise TypeError("Название, должно быть строкой!")


class Pet(Animal):
    name = Descriptor()

    def __init__(self, name, animal, age=1):
        self.name = name
        self.animal = animal
        self.age = age

    def __getattribute__(self, item):
        ''' Прототип дандер-метода __getattribute__.'''

        for cls in Pet.__mro__:

            if item in cls.__dict__:  # есть ли атрибут в пространстве имен класса.

                item_class_dict = type(cls.__dict__[item]).__dict__  # Пространства имен класса нашего атрибута

                if "__get__" in item_class_dict:  # Является ли атрибут, дескриптором.
                    return cls.__dict__[item].__get__(self, cls)

                return cls.__dict__[item]
        else:

            if item in self.__dict__:  # есть ли атрибут в пространстве имен экземпляра класса
                return self.__dict__[item]

            if "__getattr__" in self.__class__.__dict__:  # Есть ли у класса, дандер-метод __getattr__
                return self.__getattr__(item)

            raise AttributeError

    def meow(self):
        return "Meowwww!!!!" if self.animal.lower() == "cat" else "You're pet isn't cat!"


cat_kit = Pet("Kit", "Cat", 17)
print(cat_kit.name)  # Kit

print(cat_kit.animal)  # Cat

print(cat_kit.meow())  # Meowwww!
print(cat_kit.meow)  # <bound method Pet.meow of <__main__.Pet object at 0x7f940fe2f1f0>>

print(cat_kit.eyes)  # 2

print(cat_kit.eat("Kitekat"))  # "Yum, yum, yum (Kitekat)"
print(cat_kit.eat)  # <bound method Animal.eat of <__main__.Pet object at 0x7f940fe2f1f0>>

# cat_kit.dog





# def __getattribute__(self, item):
#     ''' Прототип дандер-метода __getattribute__.'''
#     for cls in Class.__mro__:
#         if item in cls.__dict__:  # есть ли атрибут в пространстве имен класса.
#             item_class_dict = type(cls.__dict__[item]).__dict__  # Пространства имен класса нашего атрибута
#             if "__get__" in item_class_dict:  # Является ли атрибут, дескриптором.
#                 return cls.__dict__[item].__get__(self, cls)
#             return cls.__dict__[item]
#         else:
#             if item in self.__dict__:  # есть ли атрибут в пространстве имен экземпляра класса
#                 return self.__dict__[item]
#             if "__getattr__" in self.__class__.__dict__:  # Есть ли у класса, дандер-метод __getattr__
#                 return self.__getattr__(item)
#             raise AttributeError