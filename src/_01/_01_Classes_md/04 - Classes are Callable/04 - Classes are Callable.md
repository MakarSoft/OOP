[Classes are Callable](https://github.com/fbaptiste/python-deepdive/blob/main/Part%204/Section%2002%20-%20Classes/04%20-%20Classes%20are%20Callable.ipynb)

### Classes are Callable

Как мы видели ранее, одна из вещей, которую Python делает для нас, когда мы создаем класс, — это делает его вызываемым.

Вызов класса создает новый экземпляр класса — объект этого конкретного типа.

```Python
class Program:
    language = 'Python'
    
    def say_hello():
        print(f'Hello from {Program.language}!')
```

```Python
p = Program()
```

```Python
type(p)
```

```
__main__.Program
```

```Python
isinstance(p, Program)
```

```
True
```

Эти экземпляры имеют собственное пространство имен и собственный `__dict__`, который отличается от класса `__dict__`:

```Python
p.__dict__
```

```
{}
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

Экземпляры также имеют атрибуты, которые могут быть не видны в их `__dict__` (они хранятся в другом месте, как мы рассмотрим позже):

```Python
p.__class__
```

```
__main__.Program
```

Хотя мы можем использовать `__class__`, мы также можем использовать `type`:

```Python
type(p) is p.__class__
```

```
True
```

Обычно мы используем `type` вместо `__class__`, точно так же, как мы обычно используем `len()` вместо доступа к `__len__`.

Почему? Ну, одна из причин в том, что люди могут возиться с атрибутом `__class__`:

```Python
class MyClass:
    pass
```

```Python
m = MyClass()
```

```Python
type(m), m.__class__
```

```
(__main__.MyClass, __main__.MyClass)
```

Но посмотрите, что здесь происходит:

Пререопределяем атрибут `__class__`
```Python
class MyClass:
    __class__ = str
```

Создаём экземпляр класса `MyClass`
```Python
m = MyClass()
```

```Python
type(m), m.__class__
```

```
(__main__.MyClass, str)
```

Так что, как видите, `type` не обманул - безопаснее использовать `type()` !

```Python
isinstance(m, MyClass)

True
```

```Python
isinstance(m, str)

True
```

---
