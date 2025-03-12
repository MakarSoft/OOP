
[Initializing Class Instances](https://github.com/fbaptiste/python-deepdive/blob/main/Part%204/Section%2002%20-%20Classes/07%20-%20Initializing%20Class%20Instances.ipynb)

### Initializing Class Instances

Когда мы создаем новый экземпляр класса, происходят две отдельные вещи:

1. Экземпляр объекта **создается**
2. Затем экземпляр объекта дополнительно **инициализируется**

Мы можем «перехватить» как этапы создания, так и этапы инициализации, используя специальные методы `__new__` и `__init__`.

Мы вернемся к `__new__` позже. Сейчас мы сосредоточимся на `__init__`.

Важно помнить, что `__init__` является **методом экземпляра**. К моменту вызова `__init__` новый объект **уже** создан, и наша функция `__init__` , определенная в классе, теперь рассматривается как **метод**, привязанный к экземпляру.

```Python
class Person:
    def __init__(self):
        print(f'Initializing a new Person object: {self}')
```

```Python
p = Person()
```

```
Initializing a new Person object: <__main__.Person object at 0x7f80a022b0f0>
```

И мы видим, что `p` имеет тот же адрес памяти:

```Python
hex(id(p))
```

```
'0x7f80a022b0f0'
```

Поскольку `__init__` является методом экземпляра, у нас есть доступ к состоянию объекта (экземпляра) внутри метода, поэтому мы можем использовать его для управления состоянием объекта:

```Python
class Person:
    def __init__(self, name):
        self.name = name
```

```Python
p = Person('Eric')
```

```Python
p.__dict__
```

```
{'name': 'Eric'}
```

На самом деле происходит следующее: после создания нового экземпляра Python видит и автоматически вызывает `<instance>.__init__(self, *args, **kwargs)`

Так что это ничем не отличается от того, если бы мы сделали это следующим образом:

```Python
class Person:
    def initialize(self, name):
        self.name = name
```

```Python
p = Person()
```

```Python
p.__dict__
```

```
{}
```

```Python
p.initialize('Eric')
```

```Python
p.__dict__
```

```
{'name': 'Eric'}
```

Но при использовании метода `__init__` обе эти вещи выполняются для нас автоматически.

Просто помните, что к моменту вызова `__init__` экземпляр уже **был** создан, а `__init__` является методом экземпляра.

---
