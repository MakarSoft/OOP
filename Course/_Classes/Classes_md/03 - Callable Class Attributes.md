[03 - Callable Class Attributes](https://github.com/fbaptiste/python-deepdive/blob/main/Part%204/Section%2002%20-%20Classes/03%20-%20Callable%20Class%20Attributes.ipynb)

### Callable Class Attributes

Атрибуты класса могут быть объектами любого типа, включая вызываемые объекты, такие как функции:

```Python
class Program:
    language = 'Python'
    
    def say_hello():
        print(f'Hello from {Program.language}!')
```

```Python
Program.__dict__
```

```
mappingproxy(
	{
		'__module__': '__main__',
        'language': 'Python',
        'say_hello': <function __main__.Program.say_hello()>,
        '__dict__': <attribute '__dict__' of 'Program' objects>,
        '__weakref__': <attribute '__weakref__' of 'Program' objects>,
        '__doc__': None
    }
)
```

Как мы видим, символ `say_hello` находится в словаре класса.

Мы также можем получить его, используя `getattr` или точечную нотацию:

```Python
Program.say_hello, getattr(Program, 'say_hello')
```

```
(
	<function __main__.Program.say_hello()>,
	<function __main__.Program.say_hello()>
)
```

И, конечно, мы можем вызвать его, поскольку он является вызываемым:

```Python
Program.say_hello()
```

```
Hello from Python!
```

```Python
getattr(Program, 'say_hello')()
```

```
Hello from Python!
```

Мы даже можем получить к нему доступ через словарь пространства имен:

```Python
Program.__dict__['say_hello']()
```

```
Hello from Python!
```


---
