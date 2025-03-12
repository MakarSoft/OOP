from pprint import pprint 
# проблема ромбовидного наследования ...
class Person:
    def hello(self):
        print("I am Person")

class Student(Person):
    def hello(self):
        print("I am Student")

class Prof(Person):
    def hello(self):
        print("I am Prof")

class Someone(Student, Prof):
    pass

s = Someone()
s.hello()

# mro() - Method Resolution Order

mro = s.__class__.mro()
pprint(mro)
# [<class '__main__.Someone'>,
#  <class '__main__.Student'>,
#  <class '__main__.Prof'>,
#  <class '__main__.Person'>,
#  <class 'object'>]


