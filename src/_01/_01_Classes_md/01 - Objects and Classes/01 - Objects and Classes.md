
[Objects and Classes](https://github.com/fbaptiste/python-deepdive/blob/main/Part%204/Section%2002%20-%20Classes/01%20-%20Objects%20and%20Classes.ipynb)

### Objects and Classes

Класс — это тип объекта. В Python мы создаем классы, используя ключевое слово `class`.

```Python
class Person:
    pass
```

Этот класс не делает ничего особенного, но он является объектом типа `type` (который сам по себе является объектом).

```Python
type(Person)
```

```
type
```

```Python
type(type)
```

```
type
```

Классы имеют «встроенные» атрибуты, хотя мы сами специально не добавляли их в класс.

Например, у них есть имя:

```Python
Person.__name__
```

```
'Person'
```

Они также являются вызываемыми, и вызов класса приводит к созданию и возврату нового **экземпляра** этого класса:

```Python
p = Person()
```

Теперь типом объекта является класс, используемый для создания этого объекта:

```Python
type(p)
```

```
__main__.Person
```

Эти экземпляры также имеют «встроенные» свойства, которые мы рассмотрим на протяжении всего курса.

Например, у них есть свойство `__class__`, которое сообщает нам, какой класс использовался для создания экземпляра:

```Python
p.__class__
```

```
__main__.Person
```

Как вы можете видеть, `p.__class__`  возвращает объект класса, используемый для создания экземпляра `p`.

Фактически:

```Python
type(p) is p.__class__
```

```
True
```

Мы также можем использовать `isinstance`, чтобы проверить, является ли объект экземпляром определенного класса — это становится немного сложнее, когда мы используем наследование, но сейчас мы этого не делаем, так что это довольно просто:

```Python
isinstance(p, Person)
```

```
True
```

```Python
isinstance(p, str)
```

```
False
```

Мы даже можем использовать `isinstance` с нашим классом, поскольку знаем, что его тип - `type`:

```Python
isinstance(Person, type)
```

```
True
```

`type` — это как бы самый общий вид объекта **класса** — мы вернемся к этому при обсуждении метапрограммирования.

Нам действительно нужно наследование, чтобы понять, как это работает, но каждый класс **является** объектом `type` (он наследует все свойства `type`).

А пока давайте просто посмотрим, какие функциональные возможности есть `type`:

```Python
help(type)
```

Справка по типу класса во встроенных модулях:

```
class type(object)
 |  type(object_or_name, bases, dict)
 |  type(object) -> the object's type
 |  type(name, bases, dict) -> a new type
 |  
 |  Methods defined here:
 |  
 |  __call__(self, /, *args, **kwargs)
 |      Call self as a function.
 |  
 |  __delattr__(self, name, /)
 |      Implement delattr(self, name).
 |  
 |  __dir__(...)
 |      __dir__() -> list
 |      specialized __dir__ implementation for types
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __instancecheck__(...)
 |      __instancecheck__() -> bool
 |      check if an object is an instance
 |  
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __prepare__(...)
 |      __prepare__() -> dict
 |      used to create the namespace for the class statement
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setattr__(self, name, value, /)
 |      Implement setattr(self, name, value).
 |  
 |  __sizeof__(...)
 |      __sizeof__() -> int
 |      return memory consumption of the type object
 |  
 |  __subclasscheck__(...)
 |      __subclasscheck__() -> bool
 |      check if a class is a subclass
 |  
 |  __subclasses__(...)
 |      __subclasses__() -> list of immediate subclasses
 |  
 |  mro(...)
 |      mro() -> list
 |      return a type's method resolution order
 |  
 |  ----------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __abstractmethods__
 |  
 |  __dict__
 |  
 |  __text_signature__
 |  
 |  ----------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __base__ = <class 'object'>
 |      The most base type
 |  
 |  __bases__ = (<class 'object'>,)
 |  
 |  __basicsize__ = 864
 |  
 |  __dictoffset__ = 264
 |  
 |  __flags__ = 2148291584
 |  
 |  __itemsize__ = 40
 |  
 |  __mro__ = (<class 'type'>, <class 'object'>)
 |  
 |  __weakrefoffset__ = 368
```

Как вы можете видеть, у него есть метод `__call__` (именно так наш класс становится вызываемым) и ряд других атрибутов и методов, которые мы увидим на протяжении всего курса.

Наши объекты класса также имеют эти свойства, потому что они наследуются от объекта `type`.

И на самом деле, `type` является экземпляром самого себя — это немного странно, и не относится к нашим собственным классам:

```Python
isinstance(type, type)
```

```
True
```

```Python
isinstance(Person, Person)
```

```
False
```

---
