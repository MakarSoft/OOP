[02 - Class Attributes](https://github.com/fbaptiste/python-deepdive/blob/main/Part%204/Section%2002%20-%20Classes/02%20-%20Class%20Attributes.ipynb)

### Class Attributes

Как мы видели, когда мы создаем класс, Python автоматически встраивает свойства и поведение в наш объект класса, например, делая его вызываемым, а также такие свойства, как `__name__`.

```Python
class Person:
    pass
```

```
Person.__name__
```

```
'Person'
```

`__name__` — **атрибут класса**. Мы можем легко добавлять собственные атрибуты класса следующим образом:

```Python
class Program:
    language = 'Python'
    version = '3.6'
```

```Python
Program.__name__
```

```
'Program'
```

```Python
Program.language
```

```
'Python'
```

```Python
Program.version
```

```
'3.6'
```

Здесь мы использовали "точечную нотацию" для доступа к атрибутам класса. Фактически, мы также можем использовать точечную нотацию для установки атрибута класса:

```Python
Program.version = '3.7'
```

```Python
Program.version
```

```
'3.7'
```

Но мы также можем использовать функции `getattr` и `setattr` для чтения и записи этих атрибутов:

```Python
getattr(Program, 'version')
```

```
'3.7'
```

```
setattr(Program, 'version', '3.6')
```

```Python
Program.version, getattr(Program, 'version')
```

```
('3.6', '3.6')
```

Python — динамический язык, и мы можем создавать атрибуты во время выполнения, вне самого определения класса:

```
Program.x = 100
```

Используя точечную нотацию, мы добавили атрибут `x` к классу Person:

```Python
Program.x, getattr(Program, 'x')
```

```
(100, 100)
```

Мы также могли бы просто использовать вызов функции `setattr`:

```Python
setattr(Program, 'y', 200)
```

```Python
Program.y, getattr(Program, 'y')
```

```
(200, 200)
```

Так где же хранится состояние? Обычно в словаре, который прикреплен к объекту **класса** (часто называемом **пространством имен** класса):

```Python
Program.__dict__
```

```
mappingproxy(
	{
		'__module__': '__main__',
        'language': 'Python',
        'version': '3.6',
        '__dict__': <attribute '__dict__' of 'Program' objects>,
        '__weakref__': <attribute '__weakref__' of 'Program' objects>,
        '__doc__': None,
        'x': 100,
        'y': 200
    }
)
```

Как вы можете видеть, этот словарь содержит наши атрибуты: `language`, `version`, `x`, `y` с соответствующими им текущими значениями.

Обратите внимание также, что `Program.__dict__` возвращает не словарь, а объект `mappingproxy` — по сути, это словарь, доступный только для чтения, который мы не можем изменять напрямую (но мы можем изменять его с помощью `setattr` или точечной нотации).

Например, если мы изменим значение атрибута:

```Python
setattr(Program, 'x', -10)
```

Мы увидим это отражение в базовом словаре:

```Python
Program.__dict__
```

```
mappingproxy(
	{
		'__module__': '__main__',
        'language': 'Python',
        'version': '3.6',
        '__dict__': <attribute '__dict__' of 'Program' objects>,
        '__weakref__': <attribute '__weakref__' of 'Program' objects>,
        '__doc__': None,
        'x': -10,
        'y': 200
    }
)
```

#### Deleting Attributes

Итак, мы можем создавать и изменять атрибуты класса во время выполнения. Можем ли мы также удалять атрибуты?

Ответ, конечно, да. Мы можем использовать ключевое слово `del` или функцию `delattr`:

```Python
del Program.x
```

```Python
Program.__dict__
```

```
mappingproxy(
	{
		'__module__': '__main__',
        'language': 'Python',
        'version': '3.6',
        '__dict__': <attribute '__dict__' of 'Program' objects>,
        '__weakref__': <attribute '__weakref__' of 'Program' objects>,
        '__doc__': None,
        'y': 200
    }
)
```

```Python
delattr(Program, 'y')
```


#### Direct Namespace Access

```Python
Program.__dict__
```

```
mappingproxy(
	{
		'__module__': '__main__',
        'language': 'Python',
        'version': '3.6',
        '__dict__': <attribute '__dict__' of 'Program' objects>,
        '__weakref__': <attribute '__weakref__' of 'Program' objects>,
        '__doc__': None
    }
)
```

Хотя `__dict__` возвращает объект `mappingproxy`, он по-прежнему является хэш-картой и по сути ведет себя как словарь, доступный только для чтения:

```Python
Program.__dict__['language']
```

```
'Python'
```

```Python
list(Program.__dict__.items())
```

```
[
	('__module__', '__main__'),
	('language', 'Python'),
	('version', '3.6'),
	('__dict__', <attribute '__dict__' of 'Program' objects>),
	('__weakref__', <attribute '__weakref__' of 'Program' objects>),
	('__doc__', None)]
```

Одно предостережение: не каждый атрибут класса находится в этом словаре (мы вернемся к этому позже).

Например, вы заметите, что атрибута `__name__` там нет:

```Python
Program.__name__
```

```
'Program'
```

```Python
"__name__" in Program.__dict__
```

```
False
```

---
