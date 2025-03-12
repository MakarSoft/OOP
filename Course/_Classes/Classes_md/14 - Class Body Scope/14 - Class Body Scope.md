[14 - Class Body Scope](https://github.com/fbaptiste/python-deepdive/blob/main/Part%204/Section%2002%20-%20Classes/14%20-%20Class%20Body%20Scope.ipynb)

### Class Body Scope

Тело класса является областью действия и, следовательно, имеет свое собственное пространство имен. Внутри этой области действия мы можем ссылаться на символы, как и в любой другой области действия:


```Python
class Language:
    MAJOR = 3
    MINOR = 7
    REVISION = 4
    FULL = '{}.{}.{}'.format(MAJOR, MINOR, REVISION)
```

```Python
Language.FULL
```

```
'3.7.4'
```

Однако функции, определенные внутри класса, не вложены в область видимости тела — вместо этого они вложены в ту область видимости, в которой находится сам класс.
Это означает, что мы не можем ссылаться на символы класса внутри функции, не указав Python также, где их искать:

```Python
class Language:
    MAJOR = 3
    MINOR = 7
    REVISION = 4
    
    @property
    def version(self):
        return '{}.{}.{}'.format(self.MAJOR, self.MINOR, self.REVISION)
    
    @classmethod
    def cls_version(cls):
        return '{}.{}.{}'.format(cls.MAJOR, cls.MINOR, cls.REVISION)
    
    @staticmethod
    def static_version():
        return '{}.{}.{}'.format(Language.MAJOR, Language.MINOR, Language.REVISION)
```

```Python
l = Language()
l.version
```

```
'3.7.4'
```

```Python
Language.cls_version()
```

```
'3.7.4'
```

```Python
Language.static_version()
```

```
'3.7.4'
```

По сути, можно подумать, что символы функций находятся в пространстве имен тела класса, но сами функции определены внешне по отношению к классу — как если бы мы написали это следующим образом:

```Python
def full_version():
 return '{}.{}.{}'.format(Language.MAJOR, Language.MINOR, Language.REVISION)
```

```Python
full_version()
```

```
'3.7.4'
```

Поэтому написать что-то вроде этого не получится:

```Python
class Language:
    MAJOR = 3
    MINOR = 7
    REVISION = 4
    
    @classmethod
    def cls_version(cls):
        return '{}.{}.{}'.format(MAJOR, MINOR, REVISION)
```

```Python
Language.cls_version()
```

```
-----------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-10-7a3f9fd88d68> in <module>
----> 1 Language.cls_version()

<ipython-input-9-18992503fb74> in cls_version(cls)
      6     @classmethod
      7     def cls_version(cls):
----> 8         return '{}.{}.{}'.format(MAJOR, MINOR, REVISION)

NameError: name 'MAJOR' is not defined
```

Такое поведение может привести к тонким ошибкам, если мы не будем осторожны.

Что произойдет, если имена `MAJOR`, `MINOR` и `REVISION` **определены** в охватывающей области?

```Python
MAJOR = 0
MINOR = 0
REVISION = 1
```

```Python
Language.cls_version()
```

```
'0.0.1'
```

Видите, что произошло?!!

Конечно, вложенные области действия следуют тем же обычным правилам, поэтому технически мы могли бы иметь что-то вроде этого:

In [13]:

```Python
MAJOR = 0
MINOR = 0
REVISION = 1

def gen_class():
    MAJOR = 0
    MINOR = 4
    REVISION = 2
    
    class Language:
        MAJOR = 3
        MINOR = 7
        REVISION = 4

        @classmethod
        def version(cls):
            return '{}.{}.{}'.format(MAJOR, MINOR, REVISION)
        
    return Language
```

```Python
cls = gen_class()
```

```Python
cls.version()
```

```
'0.4.2'
```

Обратите внимание, как область действия `version` была вложена в область действия `gen_class`, которая сама вложена в область действия `global`.

Когда мы вызвали метод `version`, он нашел `MAJOR`, `MINOR` и `REVISION` в ближайшей охватывающей области действия, которая оказалась областью действия `gen_class`.

Кстати, это означает, что `version` — это не только метод, но и замыкание.

```Python
import inspect
```

```Python
inspect.getclosurevars(cls.version)
```

```
ClosureVars(
	nonlocals={'MAJOR': 0, 'MINOR': 4, 'REVISION': 2},
	globals={},
	builtins={'format': <built-in function format>},
	unbound=set()
)
```

Последний пример «неожиданного» поведения, который я хочу вам показать, мне показал друг, которого он озадачил:

```Python
name = 'Guido'

class MyClass:
    name = 'Raymond'
    list_1 = [name] * 3
    list_2 = [name.upper() for i in range(3)]
    
    @classmethod
    def hello(cls):
        return '{} says hello'.format(name)
```

```Python
MyClass.list_1
```

```
['Raymond', 'Raymond', 'Raymond']
```

Поскольку выражение `[name] * 3` находится в теле класса, оно использует `name`, которое находит в пространстве имен класса.

```Python
MyClass.hello()
```

```
'Guido says hello'
```

Здесь `name` используется внутри функции, поэтому ближайший символ `name` — это тот, что находится в модуле/глобальной области видимости. Следовательно, мы видим, что был использован `Guido` .

```Python
MyClass.list_2
```

```
['GUIDO', 'GUIDO', 'GUIDO']
```

Это более загадочно... Почему выражение `[name.upper() for i in range(3)]` использует `name` из охватывающей (модульной/глобальной) области видимости, а не из пространства имен класса, как это делало `[name] * 3`?

Помните, что мы обсуждали о включениях?

По сути, они являются тонко завуалированными **функциями**!!!

Поэтому они ведут себя как функция, и поэтому не вложены в область видимости тела класса, а, в данном случае, в область видимости модуля/глобальной!