[12 - Deleting Properties](https://github.com/fbaptiste/python-deepdive/blob/main/Part%204/Section%2002%20-%20Classes/12%20-%20Deleting%20Properties.ipynb)

### Deleting Properties

Точно так же, как мы можем удалить атрибут из объекта экземпляра, мы также можем удалить свойство из объекта экземпляра.

Обратите внимание, что это действие просто запускает метод удаления, но свойство остается определенным **в классе**. Оно не удаляет свойство из класса, вместо этого оно обычно используется для удаления значения свойства из **экземпляра**.

Свойства, как и атрибуты, можно удалить с помощью ключевого слова `del` или функции `delattr` .

```Python
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print('getting name property value...')
        return self._name
    
    def set_name(self, value):
        print(f'setting name property to {value}...')
        self._name = value
    
    def del_name(self):
        # delete the underlying data
        print('deleting name property value...')
        del self._name
        
    name = property(fget=get_name, fset=set_name, fdel=del_name, doc='Person name.')
```

```Python
p = Person('Guido')
```

```
setting name property to Guido...
```

```Python
p.name
```

```
getting name property value...
```


```
'Guido'
```

А базовое свойство `_name` находится в нашем словаре экземпляров:

```Python
p.__dict__
```

```
{'_name': 'Guido'}
```

```Python
del p.name
```

```
deleting name property value...
```

Как мы видим, базовый атрибут `_name` больше не присутствует в словаре экземпляра:

```Python
p.__dict__
```

```
{}
```


```Python
try:
    print(p.name)
except AttributeError as ex:
    print(ex)
```

```
getting name property value...
'Person' object has no attribute '_name'
```

Как вы видите, удаление свойства не удалило определение свойства, которое все еще существует.

В качестве альтернативы мы также можем использовать функцию `delattr`:

```Python
p = Person('Raymond')
```

```
setting name property to Raymond...
```


```Python
delattr(p, 'name')
```

```
deleting name property value...
```

И, конечно, мы также можем использовать синтаксис декоратора:

```Python
class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        print('getting name property value...')
        return self._name
    
    @name.setter
    def name(self, value):
        """Person name"""
        print(f'setting name property to {value}...')
        self._name = value
    
    @name.deleter
    def name(self):
        # delete the underlying data
        print('deleting name property value...')
        del self._name
```

```Python
p = Person('Alex')
```

```
setting name property to Alex...
```


```Python
p.name
```

```
getting name property value...
```


```
'Alex'
```


```Python
del p.name
```

```
deleting name property value...
```

---
