[10 - Property Decorators](https://github.com/fbaptiste/python-deepdive/blob/main/Part%204/Section%2002%20-%20Classes/10%20-%20Property%20Decorators.ipynb)

### Property Decorators

As I explain in the lecture video, the `property` callable actually returns itself:
Как я объясняю в видеолекции, вызываемое свойство на самом деле возвращает само себя:

```Python
p = property(fget=lambda self: print('getting property'))
```

```Python
p
```

```
<property at 0x7f8348671778>
```

Как вы можете видеть, `p` — это `property`, и на самом деле это то же самое свойство, которое было создано.

Вспомните, как работают декораторы:

```Python
def my_decorator(fn):
    print('decorating function')
    def inner(*args, **kwargs):
        print('running decorated function')
        return fn(*args, **kwargs)
    return inner
```

```Python
def undecorated_function(a, b):
    print('running original function')
    return a + b
```

Теперь мы можем decorate нашу undecorated функцию следующим образом:

```Python
decorated_func = my_decorator(undecorated_function)
```
decorating function

И мы можем вызвать декорированную функцию:

```Python
decorated_func(10, 20)
```

```
running decorated function
running original function
```

```
30
```

Теперь вместо того, чтобы присваивать функции decor новый символ, мы могли бы просто повторно использовать тот же символ:

In [7]:

```Python
def my_func(a, b):
    print('running original function')
    return a + b

my_func = my_decorator(my_func)
```
decorating function

```Python
my_func(10, 20)
```

```
running decorated function
running original function
```

```
30
```

И, конечно же, это именно то, что делает синтаксис декоратора `@`:

```Python
@my_decorator
def my_func(a, b):
    print('running original function')
    return a + b
```

decorating function

```Python
my_func(10, 20)
```

```
running decorated function
running original function
```

```
30
```

Хорошо, теперь, когда мы освежили память о декораторах, мы должны быть готовы рассмотреть вызываемое свойство.

Вызываемое свойство создает объект свойства, **и возвращает его**.

Другими словами, мы могли бы создать наше свойство таким образом, как обычно:

```Python
class Person:
    def __init__(self, name):
        self._name = name
        
    def name(self):
        return self._name
    
    name = property(name)
```

```Python
p = Person('Alex')

p.name
```

```
'Alex'
```

Но вы заметите эту строку: `name = property(name)` — это именно то, что делает для нас синтаксис декоратора!

Поэтому вместо этого мы можем написать:

```Python
class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
```

```Python
p = Person('Guido')
p.name
```

```
'Guido'
```

Если вы освежите свою память на декораторе универсальной функции single dispatch, вы вспомните, что декорированная функция включала другое свойство, свойство `register`, которое само по себе было декоратором.

Ну, у объекта `property` есть некоторые свойства, например `setter`, которые по сути принимают ссылку на метод setter и также возвращают себя.
```Python
p = property(lambda self: 'getter')
```

```Python
dir(p)
```

```
['__class__',
 '__delattr__',
 '__delete__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__get__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__isabstractmethod__',
 '__le__',
 '__lt__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__set__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'deleter',
 'fdel',
 'fget',
 'fset',
 'getter',
 'setter']
```

Итак, мы можем «зарегистрировать» и установить метод, используя вызываемый метод `setter`, а также получить обратно наше свойство:
```Python
p
```

```
<property at 0x7f83581afe58>
```

```Python
p2 = p.setter(lambda self: 'setter')
```

```Python
id(p), id(p2)
```

```
(140202095607384, 140202095618152)
```

Теперь вы заметите, что идентификатор свойства изменился. Вызываемый сеттер фактически создает новое свойство (с назначенными как исходным геттером, так и новым сеттером).

Но это не имеет значения, у нас просто есть новый объект свойства, который мы можем использовать для назначения символу — и это свойство будет иметь как геттер, так и сеттер, определенные.

Давайте сделаем это вручную (сначала без синтаксиса декоратора):

```Python
class Person:
    def __init__(self, name):
        self._name = name
        
    def name(self):
        return self._name
    
    name = property(name)
    
    # creating another symbol that holds on to 
    # the name property
    name_prop = name 
    
    # because herte I'm redefining name, so we lose 
    # our original reference to the property object
    def name(self, value):
        self._name = value
        
    name = name_prop.setter(name)
    
    # finally delete name_prop which we no longer need
    del name_prop
```

```Python
Person.__dict__
```

```
mappingproxy({'__module__': '__main__',
              '__init__': <function __main__.Person.__init__(self, name)>,
              'name': <property at 0x7f83581b2bd8>,
              '__dict__': <attribute '__dict__' of 'Person' objects>,
              '__weakref__': <attribute '__weakref__' of 'Person' objects>,
              '__doc__': None})
```

И теперь у нас есть свойство `name`, которое мы создали в два этапа: сначала создаем свойство только с геттером.

Затем мы заменили наше свойство новым свойством, которое имело как геттер, так и сеттер.

```Python
p = Person('Alex')
p.name
```

```
'Alex'
```

```Python
p.name = 'Raymond'
p.name
```

```
'Raymond'
```

Надеюсь, теперь вы видите, где исходное свойство (только с геттером) имело вызываемый `сеттер`, который «добавлял» сеттер к свойству (создавая новое свойство как с геттером, так и сеттером), который также возвращал (новый) объект свойства.

Итак, мы можем упростить наш код следующим образом:

```Python
class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    # what's the property name now? --> name
    # so name has a setter callable
    @name.setter
    def name(self, value):
        self._name = value
```

Обратите внимание, что если бы мы не назвали нашу функцию-сеттер `name`, имя свойства изменилось бы!

Помните, что:

```Python
@dec
def my_func():
    pass
```

возвращает декорированную функцию с тем же именем, что и у исходной функции

```Python
Person.__dict__
```

```
mappingproxy({'__module__': '__main__',
              '__init__': <function __main__.Person.__init__(self, name)>,
              'name': <property at 0x7f83581c46d8>,
              '__dict__': <attribute '__dict__' of 'Person' objects>,
              '__weakref__': <attribute '__weakref__' of 'Person' objects>,
              '__doc__': None})
```

```Python
p = Person('Alex')
```

```Python
p.name
```

```
'Alex'
```

```Python
p.name = 'Guido'
p.name
```

```
'Guido'
```

Просто чтобы показать вам, что было бы, если бы мы не использовали то же самое имя для функции-сеттера:

```Python
class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    # property is now called name
    
    @name.setter
    def full_name(self, value):
        self._name = value
```

```Python
Person.__dict__
```

```
mappingproxy({'__module__': '__main__',
              '__init__': <function __main__.Person.__init__(self, name)>,
              'name': <property at 0x7f83581c4db8>,
              'full_name': <property at 0x7f83581c4f48>,
              '__dict__': <attribute '__dict__' of 'Person' objects>,
              '__weakref__': <attribute '__weakref__' of 'Person' objects>,
              '__doc__': None})
```
Как вы видите, теперь у нас есть два свойства в классе! Первое из них `name` будет работать только как геттер. А второе `full_name` будет работать и как геттер, и как сеттер:

```Python
p = Person('Alex')
```

```Python
p.name
```

```
'Alex'
```

```Python
p.full_name
```

```
'Alex'
```

```Python
p.full_name = 'Raymond'
```

```Python
p.full_name
```

```
'Raymond'
```

Но это не сработает:

```Python
try:
    p.name = 'Guido'
except AttributeError as ex:
    print(ex)
```

не могу задать атрибут

Технически, вызываемое свойство имеет как метод getter, так и setter — поэтому мы можем сначала создать setter, а затем «добавить» getter. Но поскольку первый аргумент для `property` — это getter, нам придется немного поработать, чтобы сделать это:

```Python
class Person:
    def __init__(self, name):
        self._name = name
        
    name = property()  # an "empty" prroperty - no getter or setter
    
    @name.setter
    def name(self, value):
        self._name = value
```

Кстати, теперь у нас есть свойство, которое можно задать, но нельзя прочитать!

```Python
p = Person('Alex')
```

```Python
p.__dict__
```

```
{'_name': 'Alex'}
```

```Python
p.name = 'Raymond'
```

```Python
p.__dict__
```

```
{'_name': 'Raymond'}
```

```Python
try:
    p.name
except AttributeError as ex:
    print(ex)
```

нечитаемый атрибут

Итак, если вам когда-нибудь понадобится атрибут, который доступен только для записи, вы можете это сделать. Возможно, данные конфиденциальны, и вы хотите установить их, но не показывать пользователям... Но данные никогда не бывают по-настоящему конфиденциальными, поэтому в лучшем случае вы их запутываете, поэтому по моему опыту мне никогда не приходилось делать что-то подобное. Просто хотел, чтобы вы это увидели, если когда-нибудь возникнет такая необходимость.

Но давайте закончим это и сделаем свойство доступным для чтения и записи:
```Python
class Person:
    def __init__(self, name):
        self._name = name
        
    name = property()  # an "empty" prroperty - no getter or setter
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @name.getter
    def name(self):
        return self._name
```

```Python
p = Person('Alex')
```

```Python
p.name
```

```
'Alex'
```

```Python
p.name = 'Raymond'
```

```Python
p.name
```

```
'Raymond'
```

Удаляющее средство работает таким же образом, и мы скоро к нему вернемся.

Наконец, вы помните, что мы могли бы настроить строку документации при использовании вызываемого `property`.

Стандартная техника заключается в том, чтобы просто определить строку документации в функции получения:

```Python
class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        """The Person's name."""
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
```

```Python
help(Person.name)
```

Help on property:

    The Person's name.

```Python
help(Person)
```

Помощь по классу Person в модуле __main__:

```
class Person(builtins.object)
 |  Methods defined here:
 |  
 |  __init__(self, name)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  name
 |      The Person's name.
```

Помощь по классу Person в модуле __main__: Что произойдет, если мы вместо этого установим его в сеттере?

```Python
class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        """The Person's name."""
        self._name = value
```

```Python
help(Person.name)
```

Help on property:

```Python
help(Person)
```

Help on class Person in module __main__:

```
class Person(builtins.object)
 |  Methods defined here:
 |  
 |  __init__(self, name)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  name[[11 - Read-Only and Computed Properties]]
```

Как вы видите, docstring свойства устанавливается только на геттере. Так как же установить docstring со свойством только для записи? Мы можем сделать это, когда создаем начальное свойство:
```Python
class Person:
    def __init__(self, name):
        self._name = name
        
    name = property(doc='Write-only name property.')
    
    @name.setter
    def name(self, value):
        self._name = value
```

```Python
help(Person.name)
```

Help on property:

    Write-only name property.

---
