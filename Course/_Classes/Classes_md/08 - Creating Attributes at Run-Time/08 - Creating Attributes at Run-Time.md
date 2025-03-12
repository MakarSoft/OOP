
[08 - Creating Attributes at Run-Time](https://github.com/fbaptiste/python-deepdive/blob/main/Part%204/Section%2002%20-%20Classes/08%20-%20Creating%20Attributes%20at%20Run-Time.ipynb)

### Creating Attributes at Run-Time

Мы уже видели, что можем добавлять атрибуты к экземплярам во время выполнения, и что это влияет только на этот один экземпляр:

```Python
class Person:
    pass
```

```Python
p1 = Person()
p2 = Person()

p1.name = 'Alex'
```

```Python
p1.__dict__
```

```
{'name': 'Alex'}
```

```Python
p2.__dict__
```

```
{}
```

Так что же произойдет, если мы добавим функцию как атрибут к нашим экземплярам напрямую (мы даже можем сделать то же самое в методе `__init__`, работает так же)?

Помните, что если мы добавим функцию к самому классу, вызов функции из экземпляра приведет к созданию метода.

Здесь результат другой, так как мы добавляем функцию напрямую к экземпляру, а не к классу:

```Python
p1.say_hello = lambda: 'Hello!'
```

```Python
p1.__dict__
```

```
{
	'name': 'Alex',
	'say_hello': <function __main__.<lambda>()>
}
```

```Python
p1.say_hello
```

```
<function __main__.<lambda>()>
```

Как видите, этот атрибут представляет собой **простую** функцию — он **не** интерпретируется как **метод**.

```Python
p1.say_hello()
```

```
'Hello!'
```

Конечно, другие экземпляры ничего не знают об этой функции:

```Python
p2.__dict__
```

```
{}
```

Итак, возникает вопрос: **можем** ли мы создать **метод** для конкретного экземпляра?

Ответ (конечно!) — да, но мы должны явно указать Python, что настраиваем метод, привязанный к этому конкретному экземпляру.

Мы делаем это, создавая объект типа `method`:

```Python
from types import MethodType
```

```Python
class Person:
    def __init__(self, name):
        self.name = name
```

```Python
p1 = Person('Eric')
p2 = Person('Alex')
```

Теперь давайте создадим объект `method` и привяжем его к `p1`. Сначала мы создадим функцию, которая будет обрабатывать привязанный объект в качестве своего первого аргумента, и используем свойство `name` экземпляра.

```Python
def say_hello(self):
    return f'{self.name} says hello!'
```

Теперь мы можем использовать эту функцию просто так, передавая ей любой объект, имеющий атрибут `name`:

```Python
say_hello(p1), say_hello(p2)
```

```
('Eric says hello!', 'Alex says hello!')
```

Однако теперь мы собираемся создать метод, привязанный конкретно к `p1`:

```Python
p1_say_hello = MethodType(say_hello, p1)
```

```Python
p1_say_hello
```

```
<bound method say_hello of <__main__.Person object at 0x7f9750295630>>
```

Как вы видите, этот метод привязан к экземпляру `p1`. Но как нам его вызвать?

Если мы попытаемся использовать точечную нотацию или `getattr`, это не сработает, потому что объект `p1` ничего не знает об этом методе:

```Python
try:
    p1.p1_say_hello()
except AttributeError as ex:
    print(ex)
```

```
'Person' object has no attribute 'p1_say_hello'
```

Все, что нам нужно сделать, это добавить этот метод в словарь экземпляров, дав ему любое имя, которое мы хотим:

```Python
p1.say_hello = p1_say_hello
```

```Python
p1.__dict__
```

```
{
	'name': 'Eric',
	'say_hello': <bound method say_hello of <__main__.Person object at 0x7f9750295630>>
}
```

Хорошо, теперь наш экземпляр знает о методе, который мы сохранили под именем `say_hello`:

```Python
p1.say_hello()
```

```
'Eric says hello!'
```

или мы можем использовать функцию `getattr`:

```Python
getattr(p1, 'say_hello')()
```

```
'Eric says hello!'
```

И, конечно же, другие инстанции ничего об этом не знают:

```Python
p2.__dict__
```

```
{'name': 'Alex'}
```

Итак, чтобы создать связанный метод после того, как объект изначально был создан, мы просто создаем связанный метод и добавляем его к самому экземпляру.

Мы можем сделать это следующим образом (то, что мы только что видели):
```Python
p1 = Person('Alex')
p1.__dict__
```

```
{'name': 'Alex'}
```

```Python
p1.say_hello = MethodType(
	lambda self: f'{self.name} says hello',
	p1
)
```

```Python
p1.say_hello()
```

```
'Alex says hello'
```

Но мы также можем сделать это из любого метода экземпляра.

#### Example

Предположим, мы хотим, чтобы некоторый класс имел некоторую функциональность, которая вызывается одинаково, но будет отличаться от экземпляра к экземпляру. Хотя мы могли бы использовать наследование, здесь я хочу какой-то подход 'plug-in', и мы можем сделать это без наследования, миксинов или чего-то подобного!

```Python
from types import MethodType

class Person:
    def __init__(self, name):
        self.name = name
        
    def register_do_work(self, func):
        setattr(self, '_do_work', MethodType(func, self))
        
    def do_work(self):
        do_work_method = getattr(self, '_do_work', None)
        # if attribute exists we'll get it back,
        #   otherwise it will be None
        if do_work_method:
            return do_work_method()
        else:
            raise AttributeError(
	            'You must first register a do_work method'
	        )
```

```Python
math_teacher = Person('Eric')
english_teacher = Person('John')
```

В данный момент ни учитель математики, ни учитель английского языка не могут выполнять работу, поскольку мы еще не «зарегистрировали» работника:

```Python
try:
    math_teacher.do_work()
except AttributeError as ex:
    print(ex)
```

Сначала нужно зарегистрировать метод do_work

Хорошо, давайте сделаем это:
```Python
def work_math(self):
     return f'{self.name} will teach differentials today.'
```

```Python
math_teacher.register_do_work(work_math)
```

```Python
math_teacher.__dict__
```

```
{
	'name': 'Eric',
	'_do_work': <bound method work_math of <__main__.Person object at 0x7f97584cdac8>>
}
```

```Python
math_teacher.do_work()
```

```
'Eric will teach differentials today.'
```

И мы можем создать другой метод `do_work` для учителя английского языка:

```Python
def work_english(self):
    return f'{self.name} will analyze Hamlet today.'
```

```Python
english_teacher.register_do_work(work_english)
```

```Python
english_teacher.do_work()
```

```
'John will analyze Hamlet today.'
```

---
