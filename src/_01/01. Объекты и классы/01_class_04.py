from typing import Optional
from pprint import pprint


class Thinker:
    '''Думатель'''
    
    answer: Optional[int] = None
    
Thinker.answer = 42

print(Thinker.__name__)
print(Thinker.__bases__)
pprint(Thinker.__dict__)


class MyClass1:
    x = 10
    y = x + 32
    
print(f'{MyClass1.x=}, {MyClass1.y=}')


class MyClass2:
    x = 10
    def my_method(_):
        print(MyClass2.x)
        
MyClass2().my_method()    
print(type(MyClass2.my_method))    
print(MyClass2.my_method)


class MyClass3:
    def hello(self):
        print('Hello World')
        
