# mixin - примись
# маленькие классы, которые имеют не очень большой набор фичь и 
# котоые как бы подмешиваются к другим классам, за счет того что 
# они тоже становятся родителями этого класса
# Предполагается их использовать только с другими классами для
# кастомизации или расширения функционала дочерних классов.
# Создание экземпляров у минсинов не предполагается...

from pprint import pprint 

class FoodMixin:
    food = None

    def get_food(self):
        if self.food is None:
            raise ValueError('Food should be set')
        print(f'I Like {self.food}')

class Person:
    def hello(self):
        print("I am Person")

class Student(FoodMixin, Person):
    food = 'Pizza'

    def hello(self):
        print("I am Student")

s = Student()
s.get_food()

# когда надо обеспечить какой-то класс дополнительной, но не очень обязательной (опциональной) функциональностью
# или когда нужно добавить одну конкретную фичу большому кол-ву не связанных родственными узами классов

