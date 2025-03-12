[09 - Properties](https://github.com/fbaptiste/python-deepdive/blob/main/Part%204/Section%2002%20-%20Classes/09%20-%20Properties.ipynb)

### Properties

Чтобы было ясно, здесь мы рассматриваем свойства **экземпляра**. То есть мы определяем свойство в определяемом нами классе, но само свойство будет **специфичным** для экземпляра, то есть разные экземпляры будут поддерживать разные значения для свойства. Так же, как атрибуты экземпляра. Главное отличие в том, что мы будем использовать метод доступа для получения, установки (и, при необходимости, удаления связанного значения экземпляра).

Как я уже упоминал в лекции, поскольку свойства используют ту же точечную нотацию (и те же функции `getattr`, `setattr` и `delattr` ), нам не нужно **начинать** со свойств. Часто голый атрибут работает просто отлично, и если позже мы решим, что нам нужно управлять получением/установкой/удалением значения атрибута, мы можем переключиться на свойства, не нарушая наш интерфейс класса. Это не похоже на такие языки, как Java, и поэтому в этих языках рекомендуется **всегда** использовать функции getter и setter. _Не так_ в Python!

**Свойство** в Python по сути является экземпляром класса — мы вернемся к тому, как выглядит этот класс, когда будем изучать дескрипторы. Сейчас мы будем использовать функцию `property` в Python, которая по сути является удобной вызываемой функцией.

Давайте начнем с простого примера и простого атрибута:

```Python
class Person:
    def __init__(self, name):
        self.name = name
```

Итак, этот класс имеет единственный экземпляр **атрибута**, `name`.

```Python
p = Person('Alex')
```

И мы можем получить доступ к этому атрибуту и ​​изменить его, используя либо точечную нотацию, либо методы `getattr` и `setattr`:

```Python
p.name
```

```
'Alex'
```

```Python
getattr(p, 'name')
```

```
'Alex'
```

```Python
p.name = 'John'
```

```Python
p.name
```

```
'John'
```

```Python
setattr(p, 'name', 'Eric')
```

```Python
p.name
```

```
'Eric'
```

Теперь предположим, что мы не хотим запрещать установку пустой строки или `None` для имени. Также мы потребуем, чтобы имя было строкой.

Для этого мы создадим метод экземпляра, который будет обрабатывать логику и установку значения. Мы также создадим метод экземпляра для извлечения значения атрибута.

Мы будем использовать `_name` в качестве переменной экземпляра для хранения имени.

```Python
class Person:
    def __init__(self, name):
        self.set_name(name)
        
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            # this is valid
            self._name = value.strip()
        else:
            raise ValueError('name must be a non-empty string')
```

```Python
p = Person('Alex')
```

```Python
try:
    p.set_name(100)
except ValueError as ex:
    print(ex)
```

имя должно быть непустой строкой

```Python
p.set_name('Eric')
```

```Python
p.get_name()
```

```
'Eric'
```

Конечно, наши пользователи по-прежнему могут напрямую манипулировать атрибутом, если захотят, используя «частный» атрибут `_name`. Вы не можете запретить кому-либо делать это в Python — они должны знать, что делать, но мы все хорошие программисты и знаем, что делать, а что нет!

Так, как мы настроили наш инициализатор, валидация тоже будет работать:

```Python
try:
    p = Person('')
except ValueError as ex:
    print(ex)
```

`name` должно быть непустой строкой

Итак, это работает, но немного мучительно использовать имена методов. Так что давайте вместо этого превратим это в свойство. Начнем с класса, который у нас только что был, и немного его подправим:

```Python
class Person:
    def __init__(self, name):
        self.name = name  # обратите внимание, как мы на самом деле задаем значение для имени, используя свойство!
        
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            # this is valid
            self._name = value.strip()
        else:
            raise ValueError('name must be a non-empty string')
            
    name = property(fget=get_name, fset=set_name)
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
p.name = 'Eric'
```

```Python
try:
    p.name = None
except ValueError as ex:
    print(ex)
```

имя должно быть непустой строкой

Так что теперь у нас есть преимущество использования методов доступа, без необходимости вызывать методы явно.

Фактически, даже `getattr` и `setattr` будут работать одинаково:

```Python
setattr(p, 'name', 'John')  # or p.name = 'John'
```

```Python
getattr(p, 'name')  # or simply p.name
```

```
'John'
```

Теперь давайте рассмотрим словарь экземпляра:

```Python
p.__dict__
```

```
{'_name': 'John'}
```

Вы увидите, что мы можем найти базовый атрибут "private", который мы используем для хранения имени. Но само свойство (`name`) отсутствует в словаре.

Свойство было определено в классе:

```Python
Person.__dict__
```

```
mappingproxy(
	{
		'__module__': '__main__',
        '__init__': <function __main__.Person.__init__(self, name)>,
        'get_name': <function __main__.Person.get_name(self)>,
        'set_name': <function __main__.Person.set_name(self, value)>,
        'name': <property at 0x7fbad886e138>,
        '__dict__': <attribute '__dict__' of 'Person' objects>,
        '__weakref__': <attribute '__weakref__' of 'Person' objects>,
        '__doc__': None
    }
)
```

И вы можете видеть, что его тип - `property`.

Поэтому, когда мы вводим `p.name` или `p.name = value`, Python распознает, что `'name` - это `property`, и поэтому использует методы доступа. (Как это происходит, мы увидим позже, когда будем изучать дескрипторы).

Интересно то, что даже если мы возимся со словарем экземпляра, Python не запутается - (и, как обычно в Python, то, что вы **можете** что-то сделать, не означает, что вы **должны** это делать!)

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
p.__dict__
```

```
{'_name': 'Alex'}
```

```Python
p.__dict__['name'] = 'John'
```

```Python
p.__dict__
```

```
{'_name': 'Alex', 'name': 'John'}
```

Как вы видите, теперь в нашем словаре экземпляров есть `name`.

Давайте извлечем `name` с помощью точечной нотации:

```Python
p.name
```

```
'Alex'
```

Очевидно, что это все еще использует метод getter.

И задаем имя:

```Python
p.name = 'Raymond'
```

```Python
p.__dict__
```

```
{'_name': 'Raymond', 'name': 'John'}
```

Как вы можете видеть, он использовал метод setter.

И то же самое происходит с `setattr` и `getattr`:

```Python
getattr(p, 'name')
```

```
'Raymond'
```

```Python
setattr(p, 'name', 'Python')
```

```Python
p.__dict__
```

```
{'_name': 'Python', 'name': 'John'}
```

Как вы можете видеть, метод `setattr` использовал метод установки свойств.

Для полноты картины давайте посмотрим, как работает метод удаления:

```Python
class Person:
    def __init__(self, name):
        self._name = name
        
    def get_name(self):
        print('getting name')
        return self._name
    
    def set_name(self, value):
        print('setting name')
        self._name = value
        
    def del_name(self):
        print('deleting name')
        del self._name  # or whatever "cleanup" we want to do
        
    name = property(get_name, set_name, del_name)
```

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
p.name
```

```
getting name
```

```
'Alex'
```

```Python
p.name = 'Eric'
```

```
setting name
```

```Python
p.__dict__
```

```
{'_name': 'Eric'}
```

```Python
del p.name
```

```
deleting name
```

```Python
p.__dict__
```

```
{}
```

Теперь свойство все еще существует (поскольку оно определено в классе) — все, что мы сделали, это удалили базовое значение для свойства (атрибут экземпляра `_name`):

```Python
try:
    p.name
except AttributeError as ex:
    print(ex)
```

```
getting name
'Person' object has no attribute '_name'
```
Объект 'Person' не имеет атрибута '_name'

Как видите, проблема в том, что функция getter пытается найти `_name` в атрибуте, который больше не существует. Поэтому getter и setter все еще существуют (т. е. свойство все еще существует), поэтому мы все еще можем присвоить ему:

```Python
p.name = 'Alex'
```

```
setting name
```

```Python
p.name
```

```
getting name
```

```
'Alex'
```

Последний параметр в `property` - это просто `docstring`. Так что мы могли бы сделать это:

```Python
class Person:
    """This is a Person object"""
    def __init__(self, name):
        self._name = name
        
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        self._name = value
        
    name = property(get_name, set_name, doc="The person's name.")
```

```Python
p = Person('Alex')
```

```
help(Person.name)
```

Help on property:

    The person's name.

```Python
help(Person)
```

Помощь по классу Person в модуле __main__:

```
class Person(builtins.object)
 |  This is a Person object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, name)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  get_name(self)
 |  
 |  set_name(self, value)
 |  
 |  -------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  name
 |      The person's name.
```

---
